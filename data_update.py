"""Download indicator data for all groups using the plugin registry.

Each registered data source plugin (World Bank, UN SDG, FAOSTAT)
fetches, normalizes, and caches its own indicators.
"""

import json
from pathlib import Path
from indicators_data import indicators
from plugins import get_all_plugins

# List of groups to process
GROUPS = ["lldcs", "ldcs", "sids", "g77", "brics", "eu", "oecd", "g20", "aosis", "lmcs", "lics"]

# Instantiate all plugins
plugins = get_all_plugins(indicators)


def load_group_countries(group_code):
    """Load the country list from the group JSON file."""
    path = Path("cache/groups") / f"{group_code}.json"
    data = json.loads(path.read_text())
    return data["countries"]  # list of {name, ISO, ISO3}


for group_code in GROUPS:
    countries = load_group_countries(group_code)
    print(f"\n===== Processing group: {group_code} ({len(countries)} countries) =====")

    for plugin in plugins:
        n = len(plugin.indicators)
        if n == 0:
            continue
        print(f"\n  [{plugin.SOURCE_NAME}] {n} indicators")
        plugin.download_all_indicators(group_code, countries)

    print(f"===== Completed group: {group_code} =====\n")

print("All indicator data downloads completed successfully!")
