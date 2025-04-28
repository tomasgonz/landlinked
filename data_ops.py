import json, pandas as pd
from pathlib import Path
import streamlit as st
from indicators_data import indicators

@st.cache_data
def load_group_data(indicator_id: str, group: str) -> pd.DataFrame:
    """
    Reads indicator_<group>.json, returns a DataFrame with columns
    [country_id, country_name, date, value].
    """
    path = Path(f"cache/indicators/{indicator_id}_{group}.json")
    meta, records = json.loads(path.read_text())
    df = pd.json_normalize(records)
    df = df.rename(columns={
        "country.id":   "country_id",
        "country.value":"country_name",
        "date":         "date",
        "value":        "value",
    })
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df.dropna(subset=["value"])

@st.cache_data
def compute_group_aggregate(indicator_id: str, group: str) -> pd.Series:
    df = load_group_data(indicator_id, group)
    rule = indicators[indicator_id]['agg']

    if rule == 'sum':
        result = df.groupby("date")["value"].sum()

    elif rule == 'mean':
        result = df.groupby("date")["value"].mean()

    elif rule == 'weighted':
        wgt_id = indicators[indicator_id]['weight_by']
        wdf = load_group_data(wgt_id, group)
        # merge on country & date
        m = pd.merge(
            df, wdf,
            on=["country_id","country_name","date"],
            suffixes=("","_wgt")
        )
        num = (m["value"] * m["value_wgt"]).groupby(m["date"]).sum()
        den = m.groupby("date")["value_wgt"].sum()
        result = num.div(den)
        result.name = "value"
        return [result.sort_index(), m]


    else:
        raise ValueError(f"Unknown agg rule '{rule}' for {indicator_id}")

    return [result.sort_index()]

def normalize_dictionary(data):
    # Normalize the nested dictionary data
    df = pd.json_normalize(data)
    # Flattening specific columns
    df = df.rename(columns={
        'indicator.id': 'indicator_id',
        'indicator.value': 'indicator_value',
        'country.id': 'country_id',
        'country.value': 'country_value'})

    # Remove rows with None values in the 'date' column
    df = df.dropna(subset=['value'])

    return df


