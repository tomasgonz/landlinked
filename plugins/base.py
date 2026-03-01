"""Abstract base class for data source plugins."""

import os
import json
import datetime
import concurrent.futures
from abc import ABC, abstractmethod


class DataSourcePlugin(ABC):
    """Base class that all data source plugins must implement.

    Each plugin knows how to fetch, normalize, and cache indicator data
    from a specific data source (World Bank, UN SDG, FAOSTAT, etc.).
    """

    SOURCE_NAME: str = ""
    SOURCE_URL: str = ""
    SOURCE_DB: str = ""

    def __init__(self, indicators_dict, cache_dir="./cache/indicators", cache_duration_days=30):
        self.cache_dir = cache_dir
        self.cache_duration_days = cache_duration_days
        # Filter indicators to only those belonging to this source
        self.indicators = {
            code: meta
            for code, meta in indicators_dict.items()
            if meta.get("source") == self.SOURCE_NAME
        }
        os.makedirs(self.cache_dir, exist_ok=True)

    def _get_cache_path(self, indicator_code, group_code):
        return os.path.join(self.cache_dir, f"{indicator_code}_{group_code}.json")

    def _is_cache_valid(self, cache_path):
        if not os.path.exists(cache_path):
            return False
        modified = datetime.datetime.fromtimestamp(os.path.getmtime(cache_path))
        return (datetime.datetime.now() - modified).days <= self.cache_duration_days

    @abstractmethod
    def fetch_indicator(self, indicator_code, group_code, countries):
        """Fetch indicator data from the remote API.

        Args:
            indicator_code: The indicator series code.
            group_code: The group identifier (e.g. 'lldcs').
            countries: List of dicts with keys 'name', 'ISO', 'ISO3'.

        Returns:
            [metadata_dict, records_list] in the normalized cache format,
            or None on failure.
        """
        ...

    def get_indicator(self, indicator_code, group_code, countries):
        """Return indicator data, using cache when valid."""
        if indicator_code not in self.indicators:
            return None

        cache_path = self._get_cache_path(indicator_code, group_code)
        if self._is_cache_valid(cache_path):
            with open(cache_path, "r") as f:
                return json.load(f)

        print(f"[{self.SOURCE_NAME}] Fetching {indicator_code} for group {group_code}")
        data = self.fetch_indicator(indicator_code, group_code, countries)

        if data:
            with open(cache_path, "w") as f:
                json.dump(data, f)
            return data

        return None

    def download_all_indicators(self, group_code, countries):
        """Download all indicators for a group using concurrent workers."""
        codes = list(self.indicators.keys())
        if not codes:
            return

        batch_size = 20
        max_workers = 8

        for i in range(0, len(codes), batch_size):
            batch = codes[i : i + batch_size]
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_code = {
                    executor.submit(self.get_indicator, code, group_code, countries): code
                    for code in batch
                }
                for future in concurrent.futures.as_completed(future_to_code):
                    code = future_to_code[future]
                    try:
                        result = future.result()
                        if result:
                            print(f"  ✓ {code}")
                        else:
                            print(f"  ✗ {code} (no data)")
                    except Exception as e:
                        print(f"  ! {code}: {e}")
