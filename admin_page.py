import streamlit as st
import subprocess
import os
import json
import yaml
import datetime
from pathlib import Path

from story_rendering import list_stories, load_story, save_story, delete_story, render_story
from indicators_data import indicators

# Authentication
def check_password():
    """Returns `True` if the user entered valid credentials."""
    admin_cfg = st.secrets.get("admin", {})
    valid_users = admin_cfg.get("users", {})

    def credentials_entered():
        username = st.session_state.get("login_username", "")
        password = st.session_state.get("login_password", "")
        if username in valid_users and valid_users[username] == password:
            st.session_state["authenticated"] = True
            st.session_state["admin_user"] = username
            del st.session_state["login_password"]
        else:
            st.session_state["authenticated"] = False

    if "authenticated" not in st.session_state:
        st.text_input("Username", key="login_username")
        st.text_input("Password", type="password", on_change=credentials_entered, key="login_password")
        return False
    elif not st.session_state["authenticated"]:
        st.text_input("Username", key="login_username")
        st.text_input("Password", type="password", on_change=credentials_entered, key="login_password")
        st.error("Invalid username or password")
        return False
    else:
        return True

st.set_page_config(page_title="Admin", page_icon="⚙️", layout="wide")

if not check_password():
    st.stop()

col_title, col_user = st.columns([4, 1])
with col_title:
    st.title("⚙️ Admin Dashboard")
with col_user:
    st.markdown(f"Logged in as **{st.session_state.get('admin_user', '')}**")
    if st.button("Logout"):
        del st.session_state["authenticated"]
        del st.session_state["admin_user"]
        st.rerun()

# Load config
CONFIG_PATH = Path(__file__).parent / "config.yaml"

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return yaml.safe_load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

config = load_config()

# Groups with indicator data available
GROUPS_WITH_DATA = [
    "aosis", "brics", "eu", "g20", "g77",
    "ldcs", "lics", "lldcs", "lmcs", "oecd", "sids",
]

FORMAT_OPTIONS = ["number", "currency", "people", "years"]

# Tabs for different admin functions
tab1, tab2, tab3, tab4 = st.tabs(["📊 Data Update", "⚙️ Settings", "📜 Logs", "📖 Stories"])

# Tab 1: Data Update
with tab1:
    st.header("Data Update")
    st.markdown("Trigger data updates from World Bank API and other sources.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Update Indicators")
        
        groups = ["lldcs", "ldcs", "sids", "g77", "brics", "eu", "oecd", "g20", "aosis", "lmcs", "lics"]
        selected_groups = st.multiselect("Select groups to update", groups, default=["lldcs"])
        
        if st.button("🔄 Update Selected Groups", type="primary"):
            with st.spinner("Updating indicator data..."):
                try:
                    # Import and run the update
                    from indicators import WorldBankAPI
                    from indicators_data import indicators
                    
                    api_client = WorldBankAPI(indicators)
                    progress_bar = st.progress(0)
                    
                    for i, group_code in enumerate(selected_groups):
                        st.write(f"Processing: {group_code.upper()}")
                        api_client.download_all_indicators(group_code)
                        progress_bar.progress((i + 1) / len(selected_groups))
                    
                    st.success("✅ Data update completed!")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        if st.button("🔄 Update All Groups"):
            with st.spinner("Updating all groups... This may take a while."):
                try:
                    result = subprocess.run(
                        ["/home/exedev/landlinked/venv/bin/python", "data_update.py"],
                        cwd="/home/exedev/landlinked",
                        capture_output=True,
                        text=True,
                        timeout=600
                    )
                    if result.returncode == 0:
                        st.success("✅ All data updated successfully!")
                        st.code(result.stdout)
                    else:
                        st.error(f"❌ Error: {result.stderr}")
                except subprocess.TimeoutExpired:
                    st.error("❌ Update timed out after 10 minutes")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    with col2:
        st.subheader("Cache Status")
        cache_dir = Path("/home/exedev/landlinked/cache/indicators")
        
        if cache_dir.exists():
            files = list(cache_dir.glob("*.json"))
            st.metric("Cached Files", len(files))
            
            if files:
                newest = max(files, key=os.path.getmtime)
                oldest = min(files, key=os.path.getmtime)
                st.write(f"**Newest:** {newest.name}")
                st.write(f"  *{datetime.datetime.fromtimestamp(newest.stat().st_mtime).strftime('%Y-%m-%d %H:%M')}*")
                st.write(f"**Oldest:** {oldest.name}")
                st.write(f"  *{datetime.datetime.fromtimestamp(oldest.stat().st_mtime).strftime('%Y-%m-%d %H:%M')}*")
        
        if st.button("🗑️ Clear Cache"):
            if cache_dir.exists():
                import shutil
                shutil.rmtree(cache_dir)
                cache_dir.mkdir(parents=True)
                st.success("Cache cleared!")
                st.rerun()

# Tab 2: Settings
with tab2:
    st.header("Application Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("App Settings")
        
        config['app']['group_name'] = st.text_input(
            "Default Group Name", 
            value=config['app'].get('group_name', 'LLDCs')
        )
        
        config['app']['show_group_selector'] = st.checkbox(
            "Show Group Selector",
            value=config['app'].get('show_group_selector', True)
        )
        
        config['app']['sidebar_width'] = st.slider(
            "Sidebar Width",
            min_value=200,
            max_value=500,
            value=config['app'].get('sidebar_width', 300)
        )
    
    with col2:
        st.subheader("Display Settings")
        
        if 'display' not in config:
            config['display'] = {}
        
        config['display']['show_quotes'] = st.checkbox(
            "Show Quotes",
            value=config.get('display', {}).get('show_quotes', True)
        )
        
        config['display']['display_charts'] = st.checkbox(
            "Display Charts",
            value=config.get('display', {}).get('display_charts', True)
        )
    
    st.divider()
    
    if st.button("💾 Save Settings", type="primary"):
        save_config(config)
        st.success("✅ Settings saved!")
        st.rerun()
    
    st.subheader("Current Config")
    st.code(yaml.dump(config, default_flow_style=False), language="yaml")

# Tab 3: Logs
with tab3:
    st.header("Access Logs")
    
    log_file = "/var/log/nginx/landlinked_access.log"
    
    col1, col2 = st.columns([3, 1])
    with col2:
        num_lines = st.selectbox("Lines to show", [50, 100, 200, 500], index=0)
        if st.button("🔄 Refresh"):
            st.rerun()
    
    try:
        result = subprocess.run(
            ["tail", f"-{num_lines}", log_file],
            capture_output=True,
            text=True
        )
        if result.returncode == 0 and result.stdout:
            st.code(result.stdout, language="text")
        else:
            st.info("No logs available yet or permission denied.")
    except Exception as e:
        st.error(f"Cannot read logs: {str(e)}")
    
    st.divider()
    st.subheader("Application Logs")
    
    try:
        result = subprocess.run(
            ["journalctl", "-u", "landlinked", "-n", "50", "--no-pager"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            st.code(result.stdout, language="text")
    except Exception as e:
        st.error(f"Cannot read application logs: {str(e)}")

# Tab 4: Stories
with tab4:
    st.header("Manage Data Stories")

    existing_stories = list_stories()
    story_slugs = [s["slug"] for s in existing_stories]
    story_options = ["— Create New —"] + story_slugs

    selected_slug = st.selectbox("Select a story to edit:", story_options, key="admin_story_select")

    # Initialise session state for sections
    if "story_sections" not in st.session_state:
        st.session_state["story_sections"] = []

    # Load selected story into form
    if selected_slug != "— Create New —":
        story_data = load_story(selected_slug)
        if story_data and "story_loaded_slug" not in st.session_state or st.session_state.get("story_loaded_slug") != selected_slug:
            st.session_state["story_sections"] = story_data.get("sections", [])
            st.session_state["story_loaded_slug"] = selected_slug
    else:
        if st.session_state.get("story_loaded_slug") != "__new__":
            st.session_state["story_sections"] = []
            st.session_state["story_loaded_slug"] = "__new__"
        story_data = None

    st.subheader("Metadata")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        story_title = st.text_input("Title", value=story_data["title"] if story_data else "", key="story_title")
        story_slug = st.text_input("Slug", value=story_data["slug"] if story_data else "", key="story_slug",
                                   help="URL-safe identifier, e.g. lldcs-overview")
        story_author = st.text_input("Author", value=story_data.get("author", "Tomas Gonzalez") if story_data else "Tomas Gonzalez", key="story_author")
    with col_m2:
        story_group = st.selectbox("Group", options=GROUPS_WITH_DATA,
                                   index=GROUPS_WITH_DATA.index(story_data["group_id"]) if story_data and story_data.get("group_id") in GROUPS_WITH_DATA else 0,
                                   key="story_group")
        story_published = st.checkbox("Published", value=story_data.get("published", False) if story_data else False, key="story_published")
        story_created = st.text_input("Created date", value=story_data.get("created", str(datetime.date.today())) if story_data else str(datetime.date.today()), key="story_created")

    st.divider()
    st.subheader("Sections")

    indicator_codes = list(indicators.keys())
    indicator_labels_map = {code: f"{indicators[code]['description']} [{code}]" for code in indicator_codes}

    sections = st.session_state["story_sections"]

    for idx, section in enumerate(sections):
        section_type = section.get("type", "unknown")
        with st.expander(f"Section {idx + 1}: {section_type}", expanded=False):
            # Move / Remove buttons
            btn_cols = st.columns(4)
            with btn_cols[0]:
                if idx > 0 and st.button("Move Up", key=f"up_{idx}"):
                    sections[idx], sections[idx - 1] = sections[idx - 1], sections[idx]
                    st.rerun()
            with btn_cols[1]:
                if idx < len(sections) - 1 and st.button("Move Down", key=f"down_{idx}"):
                    sections[idx], sections[idx + 1] = sections[idx + 1], sections[idx]
                    st.rerun()
            with btn_cols[2]:
                if st.button("Remove", key=f"remove_{idx}"):
                    sections.pop(idx)
                    st.rerun()

            if section_type == "narrative":
                section["content"] = st.text_area("Content (supports HTML/Markdown)", value=section.get("content", ""), height=150, key=f"narr_{idx}")

            elif section_type == "headline_metrics":
                ind_list = section.get("indicators", [])
                st.markdown(f"**{len(ind_list)} metric(s)**")
                for i, ind_spec in enumerate(ind_list):
                    ic1, ic2, ic3, ic4 = st.columns([3, 2, 2, 1])
                    with ic1:
                        current_code = ind_spec.get("code", indicator_codes[0])
                        code_idx = indicator_codes.index(current_code) if current_code in indicator_codes else 0
                        ind_spec["code"] = st.selectbox("Indicator", options=indicator_codes,
                                                        format_func=lambda c: indicator_labels_map.get(c, c),
                                                        index=code_idx, key=f"hm_code_{idx}_{i}")
                    with ic2:
                        fmt_idx = FORMAT_OPTIONS.index(ind_spec.get("format", "number")) if ind_spec.get("format") in FORMAT_OPTIONS else 0
                        ind_spec["format"] = st.selectbox("Format", options=FORMAT_OPTIONS, index=fmt_idx, key=f"hm_fmt_{idx}_{i}")
                    with ic3:
                        ind_spec["label"] = st.text_input("Label", value=ind_spec.get("label", ""), key=f"hm_lbl_{idx}_{i}")
                    with ic4:
                        if st.button("X", key=f"hm_rm_{idx}_{i}"):
                            ind_list.pop(i)
                            st.rerun()
                if st.button("+ Add metric", key=f"hm_add_{idx}"):
                    ind_list.append({"code": "SP.POP.TOTL", "format": "people", "label": "Population"})
                    st.rerun()

            elif section_type == "indicator":
                ic1, ic2 = st.columns(2)
                with ic1:
                    current_code = section.get("code", indicator_codes[0])
                    code_idx = indicator_codes.index(current_code) if current_code in indicator_codes else 0
                    section["code"] = st.selectbox("Indicator", options=indicator_codes,
                                                   format_func=lambda c: indicator_labels_map.get(c, c),
                                                   index=code_idx, key=f"ind_code_{idx}")
                with ic2:
                    fmt_idx = FORMAT_OPTIONS.index(section.get("format", "number")) if section.get("format") in FORMAT_OPTIONS else 0
                    section["format"] = st.selectbox("Format", options=FORMAT_OPTIONS, index=fmt_idx, key=f"ind_fmt_{idx}")
                section["commentary"] = st.text_area("Commentary (optional)", value=section.get("commentary", ""), height=100, key=f"ind_comm_{idx}")

            elif section_type == "comparison":
                ic1, ic2 = st.columns(2)
                with ic1:
                    current_code = section.get("code", indicator_codes[0])
                    code_idx = indicator_codes.index(current_code) if current_code in indicator_codes else 0
                    section["code"] = st.selectbox("Indicator", options=indicator_codes,
                                                   format_func=lambda c: indicator_labels_map.get(c, c),
                                                   index=code_idx, key=f"cmp_code_{idx}")
                with ic2:
                    fmt_idx = FORMAT_OPTIONS.index(section.get("format", "number")) if section.get("format") in FORMAT_OPTIONS else 0
                    section["format"] = st.selectbox("Format", options=FORMAT_OPTIONS, index=fmt_idx, key=f"cmp_fmt_{idx}")
                current_groups = section.get("groups", ["lldcs"])
                section["groups"] = st.multiselect("Compare groups", options=GROUPS_WITH_DATA,
                                                   default=[g for g in current_groups if g in GROUPS_WITH_DATA],
                                                   key=f"cmp_groups_{idx}")
                section["commentary"] = st.text_area("Commentary (optional)", value=section.get("commentary", ""), height=100, key=f"cmp_comm_{idx}")

    # Add section buttons
    st.markdown("---")
    add_cols = st.columns(4)
    with add_cols[0]:
        if st.button("+ Narrative"):
            sections.append({"type": "narrative", "content": ""})
            st.rerun()
    with add_cols[1]:
        if st.button("+ Headline Metrics"):
            sections.append({"type": "headline_metrics", "indicators": []})
            st.rerun()
    with add_cols[2]:
        if st.button("+ Indicator Chart"):
            sections.append({"type": "indicator", "code": "SP.POP.TOTL", "format": "people", "commentary": ""})
            st.rerun()
    with add_cols[3]:
        if st.button("+ Comparison Chart"):
            sections.append({"type": "comparison", "code": "SP.POP.TOTL", "format": "people", "groups": ["lldcs", "oecd"], "commentary": ""})
            st.rerun()

    st.divider()

    # Save / Delete
    save_col, delete_col = st.columns(2)
    with save_col:
        if st.button("💾 Save Story", type="primary"):
            if not story_slug.strip():
                st.error("Slug is required.")
            elif not story_title.strip():
                st.error("Title is required.")
            else:
                story_obj = {
                    "slug": story_slug.strip(),
                    "title": story_title.strip(),
                    "group_id": story_group,
                    "author": story_author.strip(),
                    "created": story_created.strip(),
                    "published": story_published,
                    "sections": sections,
                }
                save_story(story_obj)
                st.success(f"Story '{story_title}' saved!")
                st.rerun()

    with delete_col:
        if story_data and st.button("🗑️ Delete Story"):
            delete_story(selected_slug)
            st.session_state["story_loaded_slug"] = None
            st.success(f"Story '{selected_slug}' deleted.")
            st.rerun()

    # Preview
    if sections:
        with st.expander("Preview"):
            preview_story = {
                "slug": story_slug,
                "title": story_title,
                "group_id": story_group,
                "author": story_author,
                "created": story_created,
                "published": story_published,
                "sections": sections,
            }
            render_story(preview_story)
