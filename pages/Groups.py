# Groups.py  ────────────────────────────────────────────────────────────────
import io
import os
import random
import yaml
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from indicators import indicators, load_indicator_country_data_from_cache
from indicators_data import categorized_indicators

from groups import (
    get_group_countries_name,
    get_iso3_from_name,
    get_name_from_iso3,
    get_fips_from_iso3,
    get_iso2_from_name,
    load_group_metadata,
)

from country_facts import (
    load_country_data,
    load_factbook_data,
    country_small_flags,
    get_small_flag,
    get_country_description,
)

from quotes import quotes
from maps import create_map_from_dms
from streamlit_folium import st_folium
from data_ops import normalize_dictionary, compute_group_aggregate
from css import css_general, css_menu

# ───────────────────────────────── Page config ────────────────────────────
st.set_page_config(page_title="Indicator Dashboard", page_icon="📊", layout="wide")

# ───────────────────────────── Custom CSS ─────────────────────────────────
st.markdown(css_general, unsafe_allow_html=True)

# --- Function helpers -----------------------------------------------------
def to_excel(df: pd.DataFrame) -> bytes:
    """Return DF as in-memory .xlsx bytes."""
    out = io.BytesIO()
    with pd.ExcelWriter(out, engine="openpyxl") as writer:
        df.to_excel(writer, index=True, sheet_name="Sheet1")
    return out.getvalue()


def display_chart(data, title, source):
    if data is None:
        return
    with st.container(border=True):
        st.text(title)

        df = normalize_dictionary(data)
        if df.empty:
            st.write("No series data available for this country")
            return

        latest_value = df.loc[df["date"].idxmax(), "value"].round(2)
        latest_year = df.loc[df["date"].idxmax(), "date"]
        first_value = df.loc[df["date"].idxmin(), "value"].round(2)
        first_year = df.loc[df["date"].idxmin(), "date"]

        c1, c2 = st.columns(2)
        c1.metric(label=first_year, value=first_value)
        delta_pct = (((latest_value - first_value) / first_value) * 100).round(2)
        c2.metric(label=latest_year, value=latest_value, delta=delta_pct)

        st.line_chart(df, x="date", y="value")
        st.caption(f"Source: {source}")

# ------------------ Display Function for Comparison ------------------
def display_indicator_comparison_card(indicator_code: str, combined_df: pd.DataFrame):
    """
    Draws one indicator card comparing multiple groups in the main pane.
    """
    # Use indicator description as the main title for the card
    st.subheader(f"{indicators[indicator_code]['description']}")
    # List the groups being compared
    st.caption(f"Comparing: {', '.join(combined_df.columns)}")

    # Line chart - Streamlit automatically plots each column
    st.line_chart(combined_df)

    # Data area + download for the combined data
    st.dataframe(combined_df.tail(10), use_container_width=True)

    excel_bytes = to_excel(combined_df)
    # Make filename descriptive of comparison
    download_filename = f"{indicator_code}_comparison_{'_'.join(combined_df.columns)}.xlsx"

    st.download_button(
        "📥 Download comparison as Excel",
        excel_bytes,
        download_filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        # Key should be unique to the indicator being displayed on the page
        key=f"dl_comp_{indicator_code}"
    )
    st.divider()

# ----------------------------- Sidebar ------------------------------------
with st.sidebar:
    st.title("Navigation")

    selected_groups = st.multiselect(
        "Select the group of countries",
        ["LLDCs", "LDCs", "SIDS"],
        key="group",
    )

    st.divider()
    st.markdown("### Jump to category")

    category = st.radio(
        "",
        list(categorized_indicators.keys()),
        key="category",
        label_visibility="collapsed",
    )

# ─────────────────────────────── Main pane ────────────────────────────────
def main():
    # Check if groups are selected in the sidebar
    if not selected_groups:
        st.info("Select at least one group in the sidebar ⬅️ to compare.")
        st.stop() # Halt execution if no groups selected

    # Display general info about the comparison
    st.header(f"Indicator Comparison for: {', '.join(selected_groups)}")
    st.markdown("---")

    # Get the indicators for the selected category from the sidebar radio button
    indicator_codes_in_category = categorized_indicators.get(category, [])

    if not indicator_codes_in_category:
        st.warning(f"No indicators defined for category: {category}")
        return

    st.markdown(f"## {category}") # Display category title

    # Loop through indicators in the selected category (NO COLUMNS NEEDED)
    for ind_code in indicator_codes_in_category:

        if ind_code not in indicators:
            st.warning(f"Metadata missing for {ind_code}")
            st.divider()
            continue

        # --- Aggregate data for all selected groups for this indicator ---
        # st.write(f"Processing indicator: {ind_code}...") # Optional: Debug print
        all_series = {}
        for group_name in selected_groups:
            try:
                # Call the (cached) function from data_ops.py
                series_result = compute_group_aggregate(ind_code, group_name.lower())
                # Check if result is valid list/tuple and series is not empty
                if series_result and isinstance(series_result, (list, tuple)) and len(series_result) > 0 and not series_result[0].empty:
                    series_data = series_result[0]
                    series_data.name = group_name # Name series for legend/column name
                    all_series[group_name] = series_data
                # else: # Optional: Log if a specific group returned empty/invalid data
                #    print(f"Invalid/Empty series returned for {ind_code} / {group_name}")
            except Exception as e:
                # Log error for specific group aggregation failure but continue loop
                st.warning(f"Could not compute data for {ind_code} / {group_name}: {e}")

        # --- If we collected any data for *any* selected group, combine and display ---
        if all_series:
            try:
                # Combine dict of series into a single DataFrame
                combined_df = pd.concat(all_series, axis=1)
                if combined_df.empty:
                     st.info(f"Combined data is empty for '{indicators[ind_code]['description']}'.")
                     st.divider()
                     continue # Skip to next indicator if df is empty after concat

                combined_df.index.name = "date" # Ensure index is named

                # --- Call the display function for the combined data ---
                # This function now handles subheader, chart, table, download
                display_indicator_comparison_card(ind_code, combined_df)

            except Exception as e:
                # Display error specific to combining/displaying this indicator
                st.error(f"Error preparing/displaying comparison for {ind_code}: {e}")
                st.divider() # Still add divider on error
        else:
             # If NO series were successfully aggregated for this indicator across ALL selected groups
             st.info(f"No data available to compare for '{indicators[ind_code]['description']}' for the selected groups.")
             st.divider()

# --- Run the main function ---
if __name__ == "__main__":
   main()
