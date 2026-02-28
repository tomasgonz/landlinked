import openai
import streamlit as st
import yaml
import os
from dotenv import load_dotenv
import pandas as pd
from indicators import indicators, load_indicator_country_data_from_cache
from groups import get_group_countries_name, get_iso3_from_name, get_name_from_iso3, get_fips_from_iso3, get_iso2_from_name
from country_facts import load_country_data, load_factbook_data, country_small_flags, get_small_flag, get_country_description
from quotes import quotes
import random
from maps import create_map_from_dms
from streamlit_folium import st_folium
from data_ops import normalize_dictionary, compute_group_aggregate
from css import css_general, css_menu

# ── Page Config (must be first Streamlit call) ────────────────────────────
st.set_page_config(page_title="Landlinked", page_icon="📊", layout="wide")

# Load the configuration file
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

load_dotenv()
openai_api_key = st.secrets["openai"]["api_key"]
openai.api_key = openai_api_key
def query_openai_api(prompt):

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {f"role": "system", "content": "You are an assistant that provides detailed country information. You are factual and neutral in tone and views. You always try to provide an informative, yet constrcutive, forward looking and positive response and to avoid discuss any controversial or political topics."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Custom CSS
st.markdown(css_general, unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────
st.sidebar.markdown("""
<div class="sidebar-brand">
    <h1>Landlinked</h1>
    <div class="brand-subtitle">From landlocked to landlinked</div>
    <div class="brand-author">by Tomas Gonzalez</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.page_link("Home.py", label="Country Profiles")
st.sidebar.page_link("pages/Groups.py", label="Groups")
st.sidebar.page_link("pages/Indicators.py", label="Indicators")
st.sidebar.page_link("pages/Stories.py", label="Stories")
st.sidebar.divider()

if config['app']['show_group_selector']:
    group_name = st.sidebar.selectbox("Select the group of countries", ["LLDCs", "LDCs", "SIDS"])
else:
    group_name = "LLDCs"

# Random quote
quote = quotes[random.randint(0, len(quotes)-1)]

st.sidebar.markdown(f"""
<div class="quote-block">
    {quote['text']}
    <span class="quote-author">— {quote['author']}</span>
</div>
""", unsafe_allow_html=True)

# Load the codes and descriptions
data = {}
for code in indicators:
    data[code] = {'source': indicators[code]['source'], 'description': indicators[code]['description']}

# Create a sidebar panel with the names of all the countries in the group
group = get_group_countries_name(group_name.lower())
group.sort()

selected_country = st.sidebar.selectbox("Select Country", group)

st.sidebar.markdown(f"### {group_name} Members")

country_items = ""
for country in group:
    iso3 = get_iso3_from_name(country, group_name.lower())
    flag = get_small_flag(iso3)
    country_items += f'<span class="sidebar-country-item">{flag} {country}</span> '

st.sidebar.markdown(country_items, unsafe_allow_html=True)

# Disclaimer
st.sidebar.markdown("""
<div class="disclaimer-text">
    The data presented here is for informational purposes only. While we strive to keep the
    information up to date and correct, we make no representations or warranties of any kind,
    express or implied, about the completeness, accuracy, reliability, suitability or availability
    with respect to the website or the information, products, services, or related graphics
    contained on the website for any purpose. Any reliance you place on such information is
    therefore strictly at your own risk.
</div>
""", unsafe_allow_html=True)

def display_chart(data, title, source):
    # Load the data for the selected country
    if data is not None:
        with st.container(border=True):
            st.markdown(f'<div class="card-title">{title}</div>', unsafe_allow_html=True)
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
                    delta_value = (((latest_value - first_value) / first_value)*100).round(2) if first_value != 0 else 0
                    st.metric(label=latest_year, value=latest_value, delta=delta_value)

                st.line_chart(df, x ='date', y='value', x_label='Date', y_label='Value')

                st.caption(f"Source: {source}")
            else:
                st.write("No series data available for this country")

if selected_country:
    selected_country_iso2 = get_iso2_from_name(selected_country)
    selected_country_iso3 = get_iso3_from_name(selected_country, group_name.lower())
    selected_country_fips = get_fips_from_iso3(selected_country_iso3)
    selected_country_profile = get_country_description(selected_country_iso3)
    country_data = load_country_data(selected_country_iso3)
    factbook_data = load_factbook_data(selected_country_fips)

    col1, col2 = st.columns([3, 1], gap="large")

    with col1:
        st.title(f" {selected_country}")

        st.markdown(f'<div class="factbook-text">{selected_country_profile}</div>', unsafe_allow_html=True)

        # AI Q&A Container
        st.markdown('<div class="ai-qa-container">', unsafe_allow_html=True)
        user_query = st.text_input(f"**What would you like to know about {selected_country}?**", "")

        if user_query:
            user_query = user_query.strip() + ". I would like this question to be answered about " + selected_country
            openai_response = query_openai_api(user_query)
            st.markdown("""
                <div class="ai-disclaimer">
                    <strong>Disclaimer:</strong> The information provided here is intended for informational
                    purposes only. It may not be accurate or up-to-date. Always verify with reliable sources.
                </div>
            """, unsafe_allow_html=True)
            st.markdown(f"{openai_response}")
        st.markdown('</div>', unsafe_allow_html=True)

        # ── Environment ───────────────────────────────────────────────
        st.markdown('<div class="section-header"><h2>Environment</h2></div>', unsafe_allow_html=True)

        st.markdown(f'<div class="factbook-text"><strong>Climate</strong><br>{factbook_data["Environment"]["Climate"]["text"]}</div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("EN.GHG.CO2.PC.CE.AR5", group_name.lower(), selected_country)
        display_chart(indicator_data, "Carbon dioxide (CO2) emissions (total) excluding LULUCF (MT CO2e)", "World Bank")

        st.markdown(f'<div class="factbook-text"><strong>Party to environmental international agreements</strong><br>{factbook_data["Environment"]["Environment - international agreements"]["party to"]["text"]}</div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("EN.ATM.CO2E.PC", group_name.lower(), selected_country)
        display_chart(indicator_data, "CO2 emissions (pc)", "World Bank")

        # ── Labor Force ───────────────────────────────────────────────
        st.markdown('<div class="section-header"><h2>Labor Force</h2></div>', unsafe_allow_html=True)

        if 'Economy' in factbook_data and \
                   'Youth unemployment rate (ages 15-24)' in factbook_data['Economy']:
            st.markdown(f'<div class="factbook-text"><strong>Youth unemployment rate</strong><br>{factbook_data["Economy"]["Youth unemployment rate (ages 15-24)"]["total"]["text"]}</div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("SL.TLF.CACT.FM.ZS", group_name.lower(), selected_country)
        display_chart(indicator_data, "Labor force participation rate for ages 15-24 (% of population)", "World Bank")

        if (text := factbook_data.get('Economy', {})
                        .get('Unemployment rate', {})
                        .get('Unemployment rate 2023', {})
                        .get('text')):
            st.markdown(f'<div class="factbook-text"><strong>Unemployment rate</strong><br>{text}</div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("SL.UEM.TOTL.ZS", group_name.lower(), selected_country)
        display_chart(indicator_data, "Unemployment, total (% of total labor force)", "World Bank")

        # ── Population ────────────────────────────────────────────────
        st.markdown('<div class="section-header"><h2>Population</h2></div>', unsafe_allow_html=True)

        if 'Population distribution' in factbook_data['People and Society']:
            st.markdown(f'<div class="factbook-text"><strong>Population</strong><br>{factbook_data["People and Society"]["Population distribution"]["text"]}</div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("SP.POP.TOTL", group_name.lower(), selected_country)
        display_chart(indicator_data, "Population, total", "World Bank")

        # ── Education ─────────────────────────────────────────────────
        st.markdown('<div class="section-header"><h2>Education</h2></div>', unsafe_allow_html=True)

        st.markdown(f'<div class="factbook-text"><strong>Education expenditure</strong><br>{factbook_data["People and Society"]["Education expenditures"]["text"]}</div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("SE.PRM.NENR", group_name.lower(), selected_country)
        display_chart(indicator_data, "Net enrollment rate, primary (% of primary school age children)", "World Bank")

        # ── Connectivity ──────────────────────────────────────────────
        st.markdown('<div class="section-header"><h2>Connectivity</h2></div>', unsafe_allow_html=True)

        st.markdown(f'<div class="factbook-text"><strong>% connected to internet</strong><br>{factbook_data["Communications"]["Internet users"]["percent of population"]["text"]}</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="factbook-text"><strong>% connected to fixed broadband</strong><br>{factbook_data["Communications"]["Broadband - fixed subscriptions"]["subscriptions per 100 inhabitants"]["text"]}</div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("IT.NET.BBND.P2", group_name.lower(), selected_country)
        display_chart(indicator_data, "Fixed broadband subscriptions (per 100 people)", "World Bank")

        # ── Economy ───────────────────────────────────────────────────
        st.markdown('<div class="section-header"><h2>Economy</h2></div>', unsafe_allow_html=True)

        st.markdown(f'<div class="factbook-text"><strong>Main manufactured products</strong><br>{factbook_data["Economy"]["Industries"]["text"]}</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="factbook-text"><strong>Main agricultural products</strong><br>{factbook_data["Economy"]["Agricultural products"]["text"]}</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-header"><h2>Macroeconomic Indicators</h2></div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("NY.GDP.MKTP.PP.CD", group_name.lower(), selected_country)
        display_chart(indicator_data, "GDP (current US$)", "World Bank")

        indicator_data = load_indicator_country_data_from_cache("NY.GDP.PCAP.PP.CD", group_name.lower(), selected_country)
        display_chart(indicator_data, "GDP per capita (current US$)", "World Bank")

        indicator_data = load_indicator_country_data_from_cache("FP.CPI.TOTL.ZG", group_name.lower(), selected_country)
        display_chart(indicator_data, "Inflation, consumer prices (annual %)", "World Bank")

        st.markdown('<div class="section-header"><h2>Trade</h2></div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("BN.CAB.XOKA.CD", group_name.lower(), selected_country)
        display_chart(indicator_data, "Current account balance (current US$)", "World Bank")

        indicator_data = load_indicator_country_data_from_cache("NE.EXP.GNFS.CD", group_name.lower(), selected_country)
        display_chart(indicator_data, "Exports of goods and services (current US$)", "World Bank")

        indicator_data = load_indicator_country_data_from_cache("NE.IMP.GNFS.CD", group_name.lower(), selected_country)
        display_chart(indicator_data, "Imports of goods and services (current US$)", "World Bank")

        st.markdown('<div class="section-header"><h2>Debt and Reserves</h2></div>', unsafe_allow_html=True)

        indicator_data = load_indicator_country_data_from_cache("DT.DOD.DECT.CD", group_name.lower(), selected_country)
        display_chart(indicator_data, "External debt (current US$)", "World Bank")

        indicator_data = load_indicator_country_data_from_cache("FI.RES.TOTL.CD", group_name.lower(), selected_country)
        display_chart(indicator_data, "Total reserves (includes gold, current US$)", "World Bank")

        indicator_data = load_indicator_country_data_from_cache("GC.DOD.TOTL.CN", group_name.lower(), selected_country)
        display_chart(indicator_data, "Central government debt, total (current LCU)", "World Bank")

    with col2:
        st.image(f"https://flagcdn.com/w320/{selected_country_iso2.lower()}.png")
        geographic_coordinates = factbook_data['Geography']['Geographic coordinates']['text']

        st.markdown(f'<div class="country-meta-item"><strong>Geographic Coordinates</strong>{geographic_coordinates}</div>', unsafe_allow_html=True)

        st.image(f"./cache/maps/{selected_country_iso2.lower()}_256.png")

        st.markdown(f'<div class="country-meta-item"><strong>Official Name</strong>{country_data[0]["name"]["official"]}</div>', unsafe_allow_html=True)

        if (country_data[0]['demonyms']):
            st.markdown(f'<div class="country-meta-item"><strong>Demonym</strong>{country_data[0]["demonyms"]["eng"]["m"]}</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="country-meta-item"><strong>Translations</strong>{country_data[0]["name"]["official"]}<br>{country_data[0]["translations"]["ara"]["official"]}<br>{country_data[0]["translations"]["zho"]["official"]}<br>{country_data[0]["translations"]["fra"]["official"]}<br>{country_data[0]["translations"]["rus"]["official"]}<br>{country_data[0]["translations"]["spa"]["official"]}</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="country-meta-item"><strong>Capital</strong>{country_data[0]["capital"][0]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="country-meta-item"><strong>Region</strong>{country_data[0]["region"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="country-meta-item"><strong>Subregion</strong>{country_data[0]["subregion"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="country-meta-item"><strong>Area</strong>{country_data[0]["area"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="country-meta-item"><strong>Population</strong>{country_data[0]["population"]}</div>', unsafe_allow_html=True)

        border_countries = [get_name_from_iso3(border) for border in country_data[0]['borders']]
        border_countries.sort()
        st.markdown(f'<div class="country-meta-item"><strong>Borders</strong>{", ".join(border_countries)}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="country-meta-item"><strong>Main Export Partners</strong>{factbook_data["Economy"]["Exports - partners"]["text"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="country-meta-item"><strong>Main Import Partners</strong>{factbook_data["Economy"]["Imports - partners"]["text"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="country-meta-item"><strong>Main Export Products</strong>{factbook_data["Economy"]["Exports - commodities"]["text"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="country-meta-item"><strong>Main Import Products</strong>{factbook_data["Economy"]["Imports - commodities"]["text"]}</div>', unsafe_allow_html=True)
