# Groups.py ───────────────────────────────────────────────────────────────────
import json
import os
import streamlit as st
from country_facts import get_small_flag
from css import css_general

# ───────────────────────────────── Page config ────────────────────────────────
st.set_page_config(page_title="Landlinked — Groups", page_icon="📊", layout="wide")
st.markdown(css_general, unsafe_allow_html=True)

GROUPS_DIR = "cache/groups"


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


# ───────────────────────────────── Helpers ────────────────────────────────────
def get_country_names(group):
    """Return list of country dicts from a group, handling both keys."""
    return group.get("countries", group.get("names", []))


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
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <h1>Landlinked</h1>
        <div class="brand-subtitle">From landlocked to landlinked</div>
        <div class="brand-author">by Tomas Gonzalez</div>
    </div>
    """, unsafe_allow_html=True)

    st.page_link("Home.py", label="Country Profiles", icon="🏠")
    st.page_link("pages/Groups.py", label="Groups", icon="🌐")
    st.page_link("pages/Indicators.py", label="Indicators", icon="📊")

    st.divider()

    selected_country = st.selectbox(
        "Select a country to explore its memberships:",
        options=["— Show all groups —"] + all_country_names,
        index=0,
        key="groups_country_select",
    )
    if selected_country == "— Show all groups —":
        selected_country = None

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

else:
    # No country selected — show all groups overview
    st.markdown("""
    <h1 style="margin-bottom:0.25rem;">Country Groups</h1>
    <p style="color:var(--text-secondary);font-size:1.05rem;">
        Overview of all country groups. Select a country in the sidebar to see its memberships.
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
