# Stories.py ──────────────────────────────────────────────────────────────────
import re
import streamlit as st
from css import css_general
from story_rendering import list_stories, load_story, render_story
from groups import load_group_metadata
from country_facts import get_small_flag

# ───────────────────────────────── Page config ────────────────────────────────
st.set_page_config(page_title="Landlinked — Stories", page_icon="📊", layout="wide")
st.markdown(css_general, unsafe_allow_html=True)

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

# ───────────────────────────────── Load stories ──────────────────────────────
all_stories = list_stories()
published_stories = [s for s in all_stories if s.get("published", False)]

# Track which story is selected via session state
if "selected_story_slug" not in st.session_state:
    st.session_state["selected_story_slug"] = None

selected_story = None
if st.session_state["selected_story_slug"]:
    selected_story = next(
        (s for s in published_stories if s["slug"] == st.session_state["selected_story_slug"]), None
    )


def strip_html(text):
    """Strip HTML tags for plain-text preview."""
    return re.sub(r"<[^>]+>", "", text)


# ───────────────────────────────── Main content ──────────────────────────────
if selected_story:
    # ── Back button ──
    if st.button("< Back to all stories"):
        st.session_state["selected_story_slug"] = None
        st.rerun()

    # ── Story detail view ──
    group_id = selected_story.get("group_id", "")

    # Group header
    try:
        group_meta = load_group_metadata(group_id)
        acronym = group_meta.get("acronym", group_id.upper())
        fullname = group_meta.get("name", "")
        classifier = group_meta.get("classifier", "")
        countries = group_meta.get("countries", group_meta.get("names", []))

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
                {classifier_badge} {len(countries)} member{"s" if len(countries) != 1 else ""}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f'<div class="country-chips">{chips_html}</div>', unsafe_allow_html=True)
    except Exception:
        pass

    st.markdown("---")

    # Story title and meta
    st.markdown(f"<h1>{selected_story['title']}</h1>", unsafe_allow_html=True)
    st.markdown(
        f'<div class="story-meta">By {selected_story.get("author", "Unknown")} '
        f'&nbsp;|&nbsp; {selected_story.get("created", "")}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Render story sections
    render_story(selected_story)

else:
    # ── Story list view ──
    st.markdown("""
    <h1 style="margin-bottom:0.25rem;">Data Stories</h1>
    <p style="color:var(--text-secondary);font-size:1.05rem;">
        Curated narratives combining data analysis with authored commentary.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if not published_stories:
        st.info("No published stories yet. Check back soon!")
    else:
        for story in published_stories:
            group_id = story.get("group_id", "")
            group_badge = group_id.upper()

            # Build preview from first narrative section
            preview = ""
            for section in story.get("sections", []):
                if section.get("type") == "narrative":
                    text = strip_html(section.get("content", ""))
                    preview = text[:250] + ("..." if len(text) > 250 else "")
                    break

            # Render card as a clickable container
            with st.container(border=True):
                st.markdown(f"""
                <div style="margin-bottom:0.25rem;">
                    <span class="classifier-badge">{group_badge}</span>
                    <span class="story-meta" style="margin-left:0.5rem;">
                        By {story.get('author', 'Unknown')} &nbsp;|&nbsp; {story.get('created', '')}
                    </span>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"### {story['title']}")
                st.markdown(f'<div class="story-preview">{preview}</div>', unsafe_allow_html=True)
                if st.button("Read story", key=f"read_{story['slug']}"):
                    st.session_state["selected_story_slug"] = story["slug"]
                    st.rerun()
