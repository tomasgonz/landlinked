# Indicators.py  ─────────────────────────────────────────────────────────────
import io
import pandas as pd
import streamlit as st

from indicators_data import indicators, categorized_indicators
from data_ops import load_group_data, compute_group_aggregate
from groups import load_group_metadata, get_group_countries_name
from country_facts import get_small_flag
from css import css_general

# ───────────────────────────────── Page config ────────────────────────────────
st.set_page_config(page_title="Landlinked — Indicators", page_icon="📊", layout="wide")
st.markdown(css_general, unsafe_allow_html=True)


# --- Helpers ------------------------------------------------------------------
def to_excel(df: pd.DataFrame) -> bytes:
    out = io.BytesIO()
    with pd.ExcelWriter(out, engine="openpyxl") as writer:
        df.to_excel(writer, index=True, sheet_name="Sheet1")
    return out.getvalue()


# Build a lookup: indicator code -> description label
indicator_labels = {
    code: f"{meta['description']}  [{code}]"
    for code, meta in indicators.items()
}
label_to_code = {v: k for k, v in indicator_labels.items()}

# ───────────────────────────────── Sidebar ────────────────────────────────────
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

    st.markdown("**Select indicators and groups to explore aggregate trends**")

    # --- Group selection ---
    available_groups = [
        "LLDCs", "LDCs", "SIDS", "g77", "oecd", "eu",
        "g20", "aosis", "lmcs", "lics", "brics", "lldcs",
    ]
    selected_groups = st.multiselect(
        "Select groups:",
        options=available_groups,
        default=["LLDCs"],
        key="ind_group_select",
    )

    # --- Group membership info ---
    if selected_groups:
        with st.expander("Group membership"):
            for grp in selected_groups:
                try:
                    meta = load_group_metadata(grp)
                    st.markdown(f"**{meta.get('acronym', grp)}** — {meta.get('name', '')}")
                    st.caption(f"Classifier: {meta.get('classifier', 'N/A')}")
                    if meta.get("description"):
                        st.markdown(f"<small>{meta['description']}</small>", unsafe_allow_html=True)
                    countries = meta.get("countries", meta.get("names", []))
                    flags_line = " ".join(
                        f"{get_small_flag(c['ISO3']) or ''} {c['name']}"
                        for c in countries
                    )
                    st.markdown(flags_line)
                    st.markdown("---")
                except Exception:
                    st.caption(f"No metadata for {grp}")

        # --- Country selection ---
        all_countries = []
        seen_countries = set()
        for grp in selected_groups:
            for name in get_group_countries_name(grp.lower()):
                if name not in seen_countries:
                    seen_countries.add(name)
                    all_countries.append(name)
        all_countries.sort()

        selected_countries = st.multiselect(
            "Overlay individual countries:",
            options=all_countries,
            default=[],
            key="ind_country_select",
            help="Select countries to plot their individual data alongside group aggregates.",
        )
    else:
        selected_countries = []

    st.divider()

    # --- Category filter (optional, multi-select) ---
    category_options = list(categorized_indicators.keys())
    selected_categories = st.multiselect(
        "Filter by categories:",
        options=category_options,
        default=[],
        key="ind_category_filter",
        help="Leave empty to show all indicators, or pick one or more categories to narrow the list.",
    )

    # Build the indicator list: union of all selected categories (or all if none picked)
    if not selected_categories:
        available_codes = list(indicators.keys())
    else:
        seen = set()
        available_codes = []
        for cat in selected_categories:
            for code in categorized_indicators.get(cat, []):
                if code not in seen:
                    seen.add(code)
                    available_codes.append(code)

    available_labels = [indicator_labels[c] for c in available_codes if c in indicator_labels]

    selected_labels = st.multiselect(
        "Select indicators:",
        options=available_labels,
        default=[],
        key="ind_indicator_select",
    )

    selected_codes = [label_to_code[lbl] for lbl in selected_labels]

# ───────────────────────────────── Main pane ──────────────────────────────────
if not selected_groups:
    st.info("Select at least one group in the sidebar to get started.")
    st.stop()

if not selected_codes:
    st.info("Select at least one indicator in the sidebar to explore.")
    st.stop()

_header_parts = [f"Groups: <strong>{', '.join(selected_groups)}</strong>"]
if selected_countries:
    _header_parts.append(f"Countries: <strong>{', '.join(selected_countries)}</strong>")
_header_parts.append(f"Indicators: {len(selected_codes)} selected")

st.markdown(f"""
<h1 style="margin-bottom: 0.25rem;">Indicators</h1>
<p style="color: #4A5568; font-size: 1rem; margin-bottom: 0.5rem;">
    {' &nbsp;|&nbsp; '.join(_header_parts)}
</p>
""", unsafe_allow_html=True)
st.markdown("---")

for ind_code in selected_codes:
    meta = indicators[ind_code]
    description = meta["description"]

    # --- Compute aggregate for each selected group ---
    all_series = {}
    for grp in selected_groups:
        try:
            result = compute_group_aggregate(ind_code, grp.lower())
            if result and isinstance(result, (list, tuple)) and len(result) > 0 and not result[0].empty:
                s = result[0]
                s.name = grp
                all_series[grp] = s
        except Exception as e:
            st.warning(f"Could not compute {ind_code} for {grp}: {e}")

    if not all_series:
        st.info(f"No data available for '{description}' in the selected groups.")
        st.divider()
        continue

    combined_df = pd.concat(all_series, axis=1)
    combined_df.index.name = "date"

    if combined_df.empty:
        st.info(f"Combined data is empty for '{description}'.")
        st.divider()
        continue

    # --- Overlay selected country series ---
    if selected_countries:
        for country_name in selected_countries:
            for grp in selected_groups:
                df_grp = load_group_data(ind_code, grp.lower())
                country_df = df_grp[df_grp["country_name"] == country_name]
                if not country_df.empty:
                    country_series = country_df.set_index("date")["value"].sort_index()
                    country_series.name = country_name
                    if country_name not in combined_df.columns:
                        combined_df = combined_df.join(country_series, how="outer")
                    break  # found data in one group, no need to check others

    # --- Card header ---
    st.markdown(f"""
    <div class="comparison-card-header">
        <h3>{description}</h3>
        <div class="card-subtitle">{ind_code} &nbsp;|&nbsp; Source: {meta['source']}</div>
    </div>
    """, unsafe_allow_html=True)

    # --- Methodology info box ---
    agg_rule = meta["agg"]
    weight_id = meta.get("weight_by")

    if agg_rule == "sum":
        method_label = "Sum"
        method_desc = "Values for all countries in the group are summed for each year."
        formula = "Aggregate(t) = &sum;<sub>c</sub> X<sub>c,t</sub>"
        weight_html = ""
    elif agg_rule == "mean":
        method_label = "Simple average (mean)"
        method_desc = "An unweighted arithmetic mean across all countries with data for each year."
        formula = "Aggregate(t) = ( &sum;<sub>c</sub> X<sub>c,t</sub> ) / N<sub>t</sub>"
        weight_html = ""
    elif agg_rule == "weighted":
        weight_desc = indicators[weight_id]["description"] if weight_id and weight_id in indicators else weight_id
        method_label = "Weighted average"
        method_desc = (
            f"Each country's value is weighted by its share of "
            f"<strong>{weight_desc}</strong> (<code>{weight_id}</code>) "
            f"within the group for that year."
        )
        formula = (
            "Aggregate(t) = "
            "&sum;<sub>c</sub> ( X<sub>c,t</sub> &times; W<sub>c,t</sub> ) "
            "/ &sum;<sub>c</sub> W<sub>c,t</sub>"
        )
        weight_source = indicators[weight_id]["source"] if weight_id and weight_id in indicators else ""
        weight_html = f"""
        <tr><td style="color:var(--text-muted);font-weight:600;white-space:nowrap;padding-right:1rem;">Weight indicator</td>
            <td><code>{weight_id}</code> &mdash; {weight_desc} (Source: {weight_source})</td></tr>
        """
    else:
        method_label = agg_rule
        method_desc = ""
        formula = ""
        weight_html = ""

    with st.expander(f"Methodology and sources — {description}"):
        st.markdown(f"""
        <table style="font-size:0.88rem;line-height:1.7;border-collapse:collapse;width:100%;">
        <tr><td style="color:var(--text-muted);font-weight:600;white-space:nowrap;padding-right:1rem;">Indicator</td>
            <td><code>{ind_code}</code></td></tr>
        <tr><td style="color:var(--text-muted);font-weight:600;white-space:nowrap;padding-right:1rem;">Description</td>
            <td>{description}</td></tr>
        <tr><td style="color:var(--text-muted);font-weight:600;white-space:nowrap;padding-right:1rem;">Source</td>
            <td>{meta['source']}</td></tr>
        <tr><td style="color:var(--text-muted);font-weight:600;white-space:nowrap;padding-right:1rem;">Aggregation method</td>
            <td><strong>{method_label}</strong> &mdash; {method_desc}</td></tr>
        <tr><td style="color:var(--text-muted);font-weight:600;white-space:nowrap;padding-right:1rem;">Formula</td>
            <td style="font-size:1rem;">{formula}</td></tr>
        {weight_html}
        </table>
        <p style="font-size:0.78rem;color:var(--text-muted);margin-top:0.75rem;">
        Where X<sub>c,t</sub> = value for country <em>c</em> in year <em>t</em>,
        N<sub>t</sub> = number of countries with data in year <em>t</em>{', W<sub>c,t</sub> = weight value for country <em>c</em> in year <em>t</em>' if agg_rule == 'weighted' else ''}.
        </p>
        """, unsafe_allow_html=True)

    # Latest values as metrics
    n_cols = min(len(combined_df.columns), 6)
    cols = st.columns(n_cols)
    for i, grp_col in enumerate(combined_df.columns):
        col_data = combined_df[grp_col].dropna()
        if col_data.empty:
            continue
        latest_val = col_data.iloc[-1]
        latest_date = col_data.index[-1]
        first_val = col_data.iloc[0]
        delta = (((latest_val - first_val) / first_val) * 100).round(2) if first_val != 0 else 0
        cols[i % n_cols].metric(
            label=f"{grp_col} ({latest_date})",
            value=round(latest_val, 2),
            delta=delta,
        )

    # Line chart
    st.line_chart(combined_df)

    # Country-level detail (expandable)
    with st.expander(f"View country-level data — {description}"):
        for grp in selected_groups:
            grp_lower = grp.lower()
            df = load_group_data(ind_code, grp_lower)
            if df.empty:
                st.caption(f"No country data for {grp}")
                continue

            # Pivot: rows = date, columns = country
            pivot = df.pivot_table(
                index="date", columns="country_name", values="value"
            )
            pivot = pivot.sort_index()

            if len(selected_groups) > 1:
                st.markdown(f"**{grp}**")
            st.dataframe(pivot, use_container_width=True)

    # Download
    excel_bytes = to_excel(combined_df)
    st.download_button(
        "Download aggregate data",
        excel_bytes,
        f"{ind_code}_{'_'.join(selected_groups)}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key=f"dl_{ind_code}",
    )
    st.divider()
