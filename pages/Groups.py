# Groups.py ───────────────────────────────────────────────────────────────────
import json
import os
import pandas as pd
import streamlit as st
from country_facts import get_small_flag
from css import css_general
from data_ops import compute_group_aggregate
from indicators_data import indicators
from story_rendering import format_value

# ───────────────────────────────── Page config ────────────────────────────────
st.set_page_config(page_title="Landlinked — Groups", page_icon="📊", layout="wide")
st.markdown(css_general, unsafe_allow_html=True)

GROUPS_DIR = "cache/groups"

GROUPS_WITH_DATA = {
    "aosis", "brics", "eu", "g20", "g77",
    "ldcs", "lics", "lldcs", "lmcs", "oecd", "sids",
}

# Key indicators for group detail view
GROUP_INDICATORS = [
    ("SP.POP.TOTL", "people"),
    ("NY.GDP.MKTP.CD", "currency"),
    ("NY.GDP.PCAP.PP.CD", "currency"),
    ("EN.GHG.CO2.MT.CE.AR5", "number"),
    ("EN.GHG.CO2.PC.CE.AR5", "number"),
    ("DT.DOD.DECT.CD", "currency"),
    ("NE.EXP.GNFS.CD", "currency"),
    ("SP.DYN.LE00.IN", "years"),
]

# Headline metrics (subset shown as top-level st.metric cards)
HEADLINE_INDICATORS = [
    ("SP.POP.TOTL", "people", "Population"),
    ("NY.GDP.MKTP.CD", "currency", "GDP"),
    ("DT.DOD.DECT.CD", "currency", "External Debt"),
    ("EN.GHG.CO2.MT.CE.AR5", "number", "CO₂ Emissions (Mt)"),
]


# ───────────────────────────────── Data loading ───────────────────────────────
@st.cache_data
def load_all_groups():
    """Load every group JSON from cache/groups/."""
    groups = []
    for filename in sorted(os.listdir(GROUPS_DIR)):
        if filename.endswith(".json"):
            with open(os.path.join(GROUPS_DIR, filename), "r") as f:
                groups.append(json.load(f))
    return groups


@st.cache_data
def build_country_index(_groups):
    """Reverse index: country name -> {iso3, iso2, groups: [...]}."""
    index = {}
    for grp in _groups:
        countries = grp.get("countries", grp.get("names", []))
        for c in countries:
            name = c.get("name", "")
            if not name:
                continue
            if name not in index:
                index[name] = {
                    "iso3": c.get("ISO3"),
                    "iso2": c.get("ISO"),
                    "groups": [],
                }
            index[name]["groups"].append({
                "gid": grp.get("gid", ""),
                "acronym": grp.get("acronym", grp.get("gid", "").upper()),
                "name": grp.get("name", ""),
            })
    return index


all_groups = load_all_groups()
country_index = build_country_index(all_groups)
all_country_names = sorted(country_index.keys())

# Build group lookup: gid -> group dict, and display options
group_by_gid = {g.get("gid", ""): g for g in all_groups}
group_display_options = [
    f"{g.get('acronym', g.get('gid', '').upper())} — {g.get('name', '')}"
    for g in all_groups
]
group_display_to_gid = {
    f"{g.get('acronym', g.get('gid', '').upper())} — {g.get('name', '')}": g.get("gid", "")
    for g in all_groups
}


# ───────────────────────────────── Helpers ────────────────────────────────────
def get_country_names(group):
    """Return list of country dicts from a group, handling both keys."""
    return group.get("countries", group.get("names", []))


def render_group_indicator(ind_code, gid, fmt_type):
    """Compute aggregate for one indicator and render header + metrics + chart."""
    meta = indicators[ind_code]
    description = meta["description"]

    try:
        result = compute_group_aggregate(ind_code, gid)
        if not result or not isinstance(result, (list, tuple)) or len(result) == 0 or result[0].empty:
            return False
        series = result[0]
    except Exception:
        return False

    first_val = series.iloc[0]
    latest_val = series.iloc[-1]
    first_date = series.index[0]
    latest_date = series.index[-1]

    if first_val != 0:
        delta_pct = ((latest_val - first_val) / abs(first_val)) * 100
    else:
        delta_pct = 0

    # Header
    st.markdown(f"""
    <div class="comparison-card-header">
        <h3>{description}</h3>
        <div class="card-subtitle">{ind_code} &nbsp;|&nbsp; Source: {meta['source']} &nbsp;|&nbsp; Aggregation: {meta['agg']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Metrics: first, latest, and change
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label=f"Earliest ({first_date})",
            value=format_value(first_val, fmt_type),
        )
    with col2:
        st.metric(
            label=f"Latest ({latest_date})",
            value=format_value(latest_val, fmt_type),
        )
    with col3:
        st.metric(
            label="Change",
            value=f"{delta_pct:+.1f}%",
        )

    # Line chart
    chart_df = series.to_frame(name=description)
    chart_df.index.name = "Year"
    st.line_chart(chart_df)

    st.caption(f"Source: {meta['source']}")
    return True


def render_group_card(group, selected_country=None, membership_gids=None):
    """Return HTML for a single group card."""
    acronym = group.get("acronym", group.get("gid", "").upper())
    fullname = group.get("name", "")
    classifier = group.get("classifier", "")
    description = group.get("description", "")
    gid = group.get("gid", "")
    countries = get_country_names(group)
    member_count = len(countries)

    # Determine card state
    if selected_country and membership_gids is not None:
        if gid in membership_gids:
            card_class = "group-card highlighted"
        else:
            card_class = "group-card dimmed"
    else:
        card_class = "group-card"

    # Build country chips
    chips_html = ""
    for c in sorted(countries, key=lambda x: x.get("name", "")):
        name = c.get("name", "")
        iso3 = c.get("ISO3")
        flag = get_small_flag(iso3) if iso3 else ""
        chip_class = "country-chip active" if name == selected_country else "country-chip"
        chips_html += f'<span class="{chip_class}">{flag} {name}</span>\n'

    # Truncate long descriptions
    desc_html = ""
    if description:
        desc_html = f'<div class="group-description">{description}</div>'

    classifier_html = ""
    if classifier:
        classifier_html = f'<span class="classifier-badge">{classifier}</span> &middot; '

    return f"""
    <div class="{card_class}">
        <div class="group-card-header">
            <span class="group-acronym">{acronym}</span>
            <span class="group-fullname">{fullname}</span>
        </div>
        <div class="group-meta">
            {classifier_html}{member_count} member{"s" if member_count != 1 else ""}
        </div>
        {desc_html}
        <div class="country-chips">
            {chips_html}
        </div>
    </div>
    """


# ───────────────────────────────── Sidebar ────────────────────────────────────

def on_country_change():
    """When a country is selected, clear the group selector."""
    if st.session_state.get("groups_country_select") != "— Show all groups —":
        st.session_state["groups_group_select"] = "— Select a group —"


def on_group_change():
    """When a group is selected, clear the country selector."""
    if st.session_state.get("groups_group_select") != "— Select a group —":
        st.session_state["groups_country_select"] = "— Show all groups —"


with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <h1>Landlinked</h1>
        <div class="brand-subtitle">From landlocked to landlinked</div>
        <div class="brand-author">by Tomas Gonzalez</div>
    </div>
    """, unsafe_allow_html=True)

    st.page_link("Home.py", label="Country Profiles")
    st.page_link("pages/Groups.py", label="Groups")
    st.page_link("pages/Indicators.py", label="Indicators")
    st.page_link("pages/Stories.py", label="Stories")

    st.divider()

    selected_country = st.selectbox(
        "Filter by country:",
        options=["— Show all groups —"] + all_country_names,
        index=0,
        key="groups_country_select",
        on_change=on_country_change,
    )
    if selected_country == "— Show all groups —":
        selected_country = None

    selected_group_label = st.selectbox(
        "Select a group for details:",
        options=["— Select a group —"] + group_display_options,
        index=0,
        key="groups_group_select",
        on_change=on_group_change,
    )
    selected_group_gid = None
    if selected_group_label != "— Select a group —":
        selected_group_gid = group_display_to_gid.get(selected_group_label)

    # Show quick summary in sidebar when a country is selected
    if selected_country:
        info = country_index.get(selected_country, {})
        iso3 = info.get("iso3")
        flag = get_small_flag(iso3) if iso3 else ""
        memberships = info.get("groups", [])
        st.markdown(f"### {flag} {selected_country}")
        st.markdown(f"Member of **{len(memberships)}** groups")
        for m in sorted(memberships, key=lambda x: x["acronym"]):
            st.caption(f"**{m['acronym']}** — {m['name']}")


# ───────────────────────────────── Main content ───────────────────────────────
if selected_country:
    # ── MODE B: Country membership view (existing) ──
    info = country_index.get(selected_country, {})
    iso3 = info.get("iso3")
    iso2 = info.get("iso2")
    flag = get_small_flag(iso3) if iso3 else ""
    memberships = info.get("groups", [])
    membership_gids = {m["gid"] for m in memberships}

    # Header
    col_flag, col_title = st.columns([1, 5])
    with col_flag:
        if iso2:
            st.image(f"https://flagcdn.com/w160/{iso2.lower()}.png", width=100)
    with col_title:
        st.markdown(f"<h1 style='margin-bottom:0.25rem;'>{flag} {selected_country}</h1>", unsafe_allow_html=True)
        st.markdown(
            f"<p style='color:var(--text-secondary);font-size:1.05rem;margin-top:0;'>"
            f"Member of <strong>{len(memberships)}</strong> out of "
            f"<strong>{len(all_groups)}</strong> groups</p>",
            unsafe_allow_html=True,
        )

    # Membership badges
    badges_html = "".join(
        f'<span class="membership-badge">{m["acronym"]}</span>'
        for m in sorted(memberships, key=lambda x: x["acronym"])
    )
    st.markdown(f'<div class="membership-summary">{badges_html}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Groups containing this country (highlighted, first)
    member_groups = [g for g in all_groups if g.get("gid", "") in membership_gids]
    other_groups = [g for g in all_groups if g.get("gid", "") not in membership_gids]

    # Display in 2 columns
    col1, col2 = st.columns(2)
    for i, grp in enumerate(member_groups + other_groups):
        card_html = render_group_card(grp, selected_country, membership_gids)
        if i % 2 == 0:
            with col1:
                st.markdown(card_html, unsafe_allow_html=True)
        else:
            with col2:
                st.markdown(card_html, unsafe_allow_html=True)

elif selected_group_gid:
    # ── MODE C: Group detail + aggregate indicators ──
    group = group_by_gid.get(selected_group_gid, {})
    acronym = group.get("acronym", selected_group_gid.upper())
    fullname = group.get("name", "")
    classifier = group.get("classifier", "")
    description = group.get("description", "")
    countries = get_country_names(group)
    member_count = len(countries)

    # Group header
    classifier_badge = ""
    if classifier:
        classifier_badge = f'<span class="classifier-badge">{classifier}</span>'

    chips_html = ""
    for c in sorted(countries, key=lambda x: x.get("name", "")):
        name = c.get("name", "")
        iso3 = c.get("ISO3")
        flag = get_small_flag(iso3) if iso3 else ""
        chips_html += f'<span class="country-chip">{flag} {name}</span>\n'

    st.markdown(f"""
    <div class="group-detail-header">
        <div class="group-card-header">
            <span class="group-acronym">{acronym}</span>
            <span class="group-fullname">{fullname}</span>
        </div>
        <div class="group-meta">
            {classifier_badge} {member_count} member{"s" if member_count != 1 else ""}
        </div>
    </div>
    """, unsafe_allow_html=True)

    if description:
        st.markdown(f'<div class="factbook-text">{description}</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="country-chips">{chips_html}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Check if aggregate data is available for this group
    if selected_group_gid not in GROUPS_WITH_DATA:
        st.info(
            f"Aggregate indicator data is not yet available for **{acronym}**. "
            f"Data is currently available for: "
            f"{', '.join(sorted(gid.upper() for gid in GROUPS_WITH_DATA))}."
        )
    else:
        # Headline metrics row
        headline_cols = st.columns(len(HEADLINE_INDICATORS))
        for col, (ind_code, fmt_type, label) in zip(headline_cols, HEADLINE_INDICATORS):
            with col:
                try:
                    result = compute_group_aggregate(ind_code, selected_group_gid)
                    if result and len(result) > 0 and not result[0].empty:
                        series = result[0]
                        latest_val = series.iloc[-1]
                        latest_date = series.index[-1]
                        st.metric(
                            label=f"{label} ({latest_date})",
                            value=format_value(latest_val, fmt_type),
                        )
                    else:
                        st.metric(label=label, value="N/A")
                except Exception:
                    st.metric(label=label, value="N/A")

        st.markdown("---")

        # Indicator sections
        rendered_any = False
        for ind_code, fmt_type in GROUP_INDICATORS:
            if render_group_indicator(ind_code, selected_group_gid, fmt_type):
                rendered_any = True
                st.divider()

        if not rendered_any:
            st.info("No indicator data could be loaded for this group.")

else:
    # ── MODE A: All groups overview (existing) ──
    st.markdown("""
    <h1 style="margin-bottom:0.25rem;">Country Groups</h1>
    <p style="color:var(--text-secondary);font-size:1.05rem;">
        Overview of all country groups. Select a country or group in the sidebar to explore.
    </p>
    """, unsafe_allow_html=True)

    # Stats
    total_countries = len(all_country_names)
    total_groups = len(all_groups)
    avg_members = sum(len(get_country_names(g)) for g in all_groups) // total_groups
    st.markdown(f"""
    <div class="groups-stats">
        <div class="groups-stat-item">
            <div class="groups-stat-value">{total_groups}</div>
            <div class="groups-stat-label">Groups</div>
        </div>
        <div class="groups-stat-item">
            <div class="groups-stat-value">{total_countries}</div>
            <div class="groups-stat-label">Countries</div>
        </div>
        <div class="groups-stat-item">
            <div class="groups-stat-value">{avg_members}</div>
            <div class="groups-stat-label">Avg members</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # All groups in 2 columns
    col1, col2 = st.columns(2)
    for i, grp in enumerate(all_groups):
        card_html = render_group_card(grp)
        if i % 2 == 0:
            with col1:
                st.markdown(card_html, unsafe_allow_html=True)
        else:
            with col2:
                st.markdown(card_html, unsafe_allow_html=True)
