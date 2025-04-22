import pandas as pd
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

    else:
        raise ValueError(f"Unknown agg rule '{rule}' for {indicator_id}")

    return result.sort_index()
