import io
import streamlit as st
import yaml
import os
from dotenv import load_dotenv
import pandas as pd
from indicators import indicators, load_indicator_country_data_from_cache
from indicators_data import categorized_indicators
from groups import get_group_countries_name, get_iso3_from_name, get_name_from_iso3, get_fips_from_iso3, get_iso2_from_name, load_group_metadata
from country_facts import load_country_data, load_factbook_data, country_small_flags, get_small_flag, get_country_description
from quotes import quotes
import random
from maps import create_map_from_dms
from streamlit_folium import st_folium
from data_ops import normalize_dictionary, compute_group_aggregate
from css import css_general, css_menu

# --- Function to convert DataFrame to Excel in memory ---
def to_excel(df):
    """Converts a DataFrame to an Excel file in memory (bytes)."""
    output = io.BytesIO()
    # Use ExcelWriter context manager for proper handling
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Write DataFrame to Excel file buffer
        # index=True includes the DataFrame index (e.g., 'w_average') in the Excel file
        df.to_excel(writer, index=True, sheet_name='Sheet1')
        # No need to explicitly save or close when using 'with' context manager

    # Get the Excel file contents as bytes
    excel_data = output.getvalue()
    return excel_data

def display_chart(data, title, source):
    # Load the data for the selected country
    if data is not None:
        with st.container(border=True):
            st.text(title)
            df = normalize_dictionary(data)
            if not df.empty:
                latest_value = df.loc[df['date'].idxmax(), 'value'].round(2)
                latest_year = df.loc[df['date'].idxmax(), 'date']
                first_value = df.loc[df['date'].idxmin(), 'value'].round(2)
                first_year = df.loc[df['date'].idxmin(), 'date']

                cola, colb = st.columns([1, 1])
                with cola:
                    st.metric(label=first_year, value=first_value)
                with colb:
                    delta_value = (((latest_value - first_value) / first_value)*100).round(2)
                    st.metric(label=latest_year, value=latest_value, delta=delta_value)

                st.line_chart(df, x ='date', y='value', x_label='Date', y_label='Value')

                st.caption(f"Source: {source}")
            else:
                st.write("No series data available for this country")

def display_group_indicator_card(INDICATOR):
    st.subheader(f"{indicators[INDICATOR]['description']} · {group_name}")
    series = compute_group_aggregate(INDICATOR,group_name.lower())
    st.line_chart(series[0])
    st.dataframe(series[0].to_frame().T)
    # --- Generate the Excel data ---
    excel_bytes = to_excel(series[0].to_frame().T)
    # --- Add the Streamlit Download Button ---
    st.download_button(
        label="📥 Download data as Excel",  # Button label
        data=excel_bytes,  # Pass the Excel data (bytes)
        file_name='weighted_average_results.xlsx',  # Default file name
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',  # MIME type for .xlsx files
        key=INDICATOR
    )
    st.divider() # Add divider after each card

# Create a sidebar panel with the names of all the countries in the group to display specific data on them
group_name = st.sidebar.selectbox("Select the group of countries", ["LLDCs", "LDCs", "SIDS"])

if group_name:

    group_metadata = load_group_metadata(group_name)

    st.header(group_name)
    st.write(group_metadata["name"])
    st.write(group_metadata["description"])

    group = get_group_countries_name(group_name.lower())
    group.sort()

    country_names = ""
    for country in group:
        iso3 = get_iso3_from_name(country, group_name.lower())
        flag = get_small_flag(iso3)
        country_names += f"{flag}\u00A0{country}  "

    st.write(country_names)

    for category in categorized_indicators:
        st.title(category)
        for indicator in categorized_indicators[category]:
            display_group_indicator_card(indicator)
