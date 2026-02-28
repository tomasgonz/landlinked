import streamlit as st
import subprocess
import os
import yaml
import datetime
from pathlib import Path

# Password protection
def check_password():
    """Returns `True` if the user had the correct password."""
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets.get("admin", {}).get("password", "admin123"):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Admin Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Admin Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        return True

st.set_page_config(page_title="Admin", page_icon="⚙️", layout="wide")
st.title("⚙️ Admin Dashboard")

if not check_password():
    st.stop()

# Load config
CONFIG_PATH = Path(__file__).parent.parent / "config.yaml"

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return yaml.safe_load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)

config = load_config()

# Tabs for different admin functions
tab1, tab2, tab3 = st.tabs(["📊 Data Update", "⚙️ Settings", "📜 Logs"])

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
