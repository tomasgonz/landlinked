# story_rendering.py — Shared module for data stories
import json
import os
import pandas as pd
import streamlit as st
from pathlib import Path

from data_ops import compute_group_aggregate
from indicators_data import indicators

STORIES_DIR = "cache/stories"


# ───────────────────────────────── Value formatting ──────────────────────────
def format_value(val, fmt_type):
    """Format a numeric value for display based on type."""
    if val is None or pd.isna(val):
        return "N/A"
    if fmt_type == "currency":
        if abs(val) >= 1e12:
            return f"${val / 1e12:.1f}T"
        elif abs(val) >= 1e9:
            return f"${val / 1e9:.1f}B"
        elif abs(val) >= 1e6:
            return f"${val / 1e6:.1f}M"
        else:
            return f"${val:,.0f}"
    elif fmt_type == "people":
        if abs(val) >= 1e9:
            return f"{val / 1e9:.2f}B"
        elif abs(val) >= 1e6:
            return f"{val / 1e6:.1f}M"
        else:
            return f"{val:,.0f}"
    elif fmt_type == "years":
        return f"{val:.1f} yrs"
    else:  # number
        if abs(val) >= 1e9:
            return f"{val / 1e9:.1f}B"
        elif abs(val) >= 1e6:
            return f"{val / 1e6:.1f}M"
        elif abs(val) >= 1e3:
            return f"{val / 1e3:.1f}K"
        else:
            return f"{val:,.1f}"


# ───────────────────────────────── Story CRUD ────────────────────────────────
def list_stories():
    """Return list of all story dicts from cache/stories/."""
    stories = []
    if not os.path.exists(STORIES_DIR):
        return stories
    for filename in sorted(os.listdir(STORIES_DIR)):
        if filename.endswith(".json"):
            path = os.path.join(STORIES_DIR, filename)
            with open(path, "r") as f:
                stories.append(json.load(f))
    return stories


def load_story(slug):
    """Load a single story by slug. Returns None if not found."""
    path = os.path.join(STORIES_DIR, f"{slug}.json")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)


def save_story(story):
    """Save a story dict to cache/stories/<slug>.json."""
    os.makedirs(STORIES_DIR, exist_ok=True)
    slug = story.get("slug", "untitled")
    path = os.path.join(STORIES_DIR, f"{slug}.json")
    with open(path, "w") as f:
        json.dump(story, f, indent=2)


def delete_story(slug):
    """Delete a story by slug."""
    path = os.path.join(STORIES_DIR, f"{slug}.json")
    if os.path.exists(path):
        os.remove(path)


# ───────────────────────────────── Section renderers ─────────────────────────
def render_narrative_section(section):
    """Render a narrative (markdown text) section."""
    content = section.get("content", "")
    st.markdown(f'<div class="factbook-text">{content}</div>', unsafe_allow_html=True)


def render_headline_metrics_section(section, group_id):
    """Render a row of headline st.metric cards."""
    ind_list = section.get("indicators", [])
    if not ind_list:
        return

    cols = st.columns(len(ind_list))
    for col, ind_spec in zip(cols, ind_list):
        code = ind_spec.get("code", "")
        fmt = ind_spec.get("format", "number")
        label = ind_spec.get("label", indicators.get(code, {}).get("description", code))

        with col:
            try:
                result = compute_group_aggregate(code, group_id)
                if result and len(result) > 0 and not result[0].empty:
                    series = result[0]
                    latest_val = series.iloc[-1]
                    latest_date = series.index[-1]
                    st.metric(
                        label=f"{label} ({latest_date})",
                        value=format_value(latest_val, fmt),
                    )
                else:
                    st.metric(label=label, value="N/A")
            except Exception:
                st.metric(label=label, value="N/A")


def render_indicator_section(section, group_id):
    """Render an indicator chart section with metrics and optional commentary."""
    code = section.get("code", "")
    fmt = section.get("format", "number")
    commentary = section.get("commentary", "")

    if code not in indicators:
        st.warning(f"Unknown indicator: {code}")
        return

    meta = indicators[code]
    description = meta["description"]

    try:
        result = compute_group_aggregate(code, group_id)
        if not result or not isinstance(result, (list, tuple)) or len(result) == 0 or result[0].empty:
            st.info(f"No data available for {description}.")
            return
        series = result[0]
    except Exception:
        st.info(f"Could not load data for {description}.")
        return

    first_val = series.iloc[0]
    latest_val = series.iloc[-1]
    first_date = series.index[0]
    latest_date = series.index[-1]
    delta_pct = ((latest_val - first_val) / abs(first_val)) * 100 if first_val != 0 else 0

    # Header
    st.markdown(f"""
    <div class="comparison-card-header">
        <h3>{description}</h3>
        <div class="card-subtitle">{code} &nbsp;|&nbsp; Source: {meta['source']} &nbsp;|&nbsp; Aggregation: {meta['agg']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label=f"Earliest ({first_date})", value=format_value(first_val, fmt))
    with col2:
        st.metric(label=f"Latest ({latest_date})", value=format_value(latest_val, fmt))
    with col3:
        st.metric(label="Change", value=f"{delta_pct:+.1f}%")

    # Line chart
    chart_df = series.to_frame(name=description)
    chart_df.index.name = "Year"
    st.line_chart(chart_df)

    st.caption(f"Source: {meta['source']}")

    # Optional commentary
    if commentary:
        st.markdown(f'<div class="factbook-text">{commentary}</div>', unsafe_allow_html=True)


GROUP_LABELS = {
    "lldcs": "LLDCs", "ldcs": "LDCs", "sids": "SIDS", "oecd": "OECD",
    "eu": "EU", "g20": "G20", "g77": "G77", "brics": "BRICS",
    "aosis": "AOSIS", "lmcs": "LMCs", "lics": "LICs",
}


def render_comparison_section(section, group_id):
    """Render a multi-group comparison chart with metrics for each group."""
    code = section.get("code", "")
    fmt = section.get("format", "number")
    commentary = section.get("commentary", "")
    compare_groups = section.get("groups", [group_id])

    if code not in indicators:
        st.warning(f"Unknown indicator: {code}")
        return

    meta = indicators[code]
    description = meta["description"]

    # Header
    st.markdown(f"""
    <div class="comparison-card-header">
        <h3>{description}</h3>
        <div class="card-subtitle">{code} &nbsp;|&nbsp; Source: {meta['source']} &nbsp;|&nbsp; Comparing: {', '.join(GROUP_LABELS.get(g, g.upper()) for g in compare_groups)}</div>
    </div>
    """, unsafe_allow_html=True)

    # Collect series for each group
    all_series = {}
    for gid in compare_groups:
        try:
            result = compute_group_aggregate(code, gid)
            if result and len(result) > 0 and not result[0].empty:
                s = result[0]
                s.name = GROUP_LABELS.get(gid, gid.upper())
                all_series[gid] = s
        except Exception:
            pass

    if not all_series:
        st.info(f"No data available for {description}.")
        return

    # Metrics row — latest value for each group
    cols = st.columns(len(all_series))
    for col, (gid, series) in zip(cols, all_series.items()):
        label = GROUP_LABELS.get(gid, gid.upper())
        latest_val = series.iloc[-1]
        latest_date = series.index[-1]
        first_val = series.iloc[0]
        delta_pct = ((latest_val - first_val) / abs(first_val)) * 100 if first_val != 0 else 0
        with col:
            st.metric(
                label=f"{label} ({latest_date})",
                value=format_value(latest_val, fmt),
                delta=f"{delta_pct:+.1f}%",
            )

    # Combined chart
    combined_df = pd.concat(all_series.values(), axis=1)
    combined_df.index.name = "Year"
    st.line_chart(combined_df)

    st.caption(f"Source: {meta['source']}")

    # Commentary
    if commentary:
        st.markdown(f'<div class="factbook-text">{commentary}</div>', unsafe_allow_html=True)


# ───────────────────────────────── Story dispatcher ──────────────────────────
def render_story(story):
    """Render all sections of a story."""
    group_id = story.get("group_id", "lldcs")
    sections = story.get("sections", [])

    for section in sections:
        section_type = section.get("type", "")
        if section_type == "narrative":
            render_narrative_section(section)
        elif section_type == "headline_metrics":
            render_headline_metrics_section(section, group_id)
        elif section_type == "indicator":
            render_indicator_section(section, group_id)
        elif section_type == "comparison":
            render_comparison_section(section, group_id)
        else:
            st.warning(f"Unknown section type: {section_type}")
