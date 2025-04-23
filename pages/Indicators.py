import io
import streamlit as st
import pandas as pd
from indicators_data import indicators
from data_ops import compute_group_aggregate
import xlsxwriter

# assume you already have these from earlier:
#   indicators: dict of your metadata (with 'agg' and optional 'weight_by')
#   load_group_data()
#   compute_group_aggregate()

st.set_page_config(page_title="Indicator Explorer", layout="wide")
st.title("Indicator Explorer")

# let them pick the group once
group = st.sidebar.selectbox(
    "Select group",
    ["lldcs", "ldcs", "sids", "all"],
)

st.markdown(
    """
    Click on any indicator below to expand and see the chart, raw data,
    how it's aggregated (sum, mean or population-weighted), and the source.
    """
)

for ind_id, meta in indicators.items():
    with st.expander(f"**{meta['description']}**"):
        # 1. show metadata
        cols = st.columns([1,3])
        cols[0].markdown(f"**Source:**\n{meta['source']}")
        cols[1].markdown(f"**Aggregation:**\n{meta['agg'].capitalize()}"
                         + (f"\n**Weighted by:** {indicators[meta['weight_by']]['description']}"
                            if meta.get("weight_by") else ""))

        # 2. compute & plot
        series = compute_group_aggregate(ind_id, group)
        st.line_chart(series[0])

        # If it is a weighted indicator
        if meta.get("weight_by"):
            st.dataframe(series[1])

        # 3. raw data table
        df = series[0].reset_index().rename(columns={"value": "Value"})
        st.dataframe(df, use_container_width=True)

        # 4. prepare Excel in memory
        towrite = io.BytesIO()
        with pd.ExcelWriter(towrite, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Data")
        towrite.seek(0)  # rewind

        # 5. download button
        st.download_button(
            label="📥 Download as Excel",
            data=towrite,
            file_name=f"{ind_id}_{group}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

