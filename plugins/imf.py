"""IMF DataMapper API plugin.

API: https://www.imf.org/external/datamapper/api/v1/{indicator}
Uses ISO3 country codes. Fetches all countries at once and filters
by group. Includes IMF forecasts (2025-2030).
"""

import time
import threading
import requests
from plugins.base import DataSourcePlugin

MAX_RETRIES = 3
RATE_LIMIT_DELAY = 0.5
REQUEST_TIMEOUT = 30


class IMFPlugin(DataSourcePlugin):
    SOURCE_NAME = "IMF"
    SOURCE_URL = "https://www.imf.org/external/datamapper"
    SOURCE_DB = "IMF DataMapper"

    def __init__(self, indicators_dict, **kwargs):
        super().__init__(indicators_dict, **kwargs)
        self.session = requests.Session()
        self.last_request_time = 0
        self._lock = threading.Lock()
        # Cache of raw indicator data: {indicator_code: {ISO3: {year: value}}}
        self._indicator_cache = {}

    def _respect_rate_limit(self):
        with self._lock:
            elapsed = time.time() - self.last_request_time
            if elapsed < RATE_LIMIT_DELAY:
                time.sleep(RATE_LIMIT_DELAY - elapsed)
            self.last_request_time = time.time()

    def _fetch_all_indicator_data(self, indicator_code):
        """Fetch all data for an indicator (all countries, all years)."""
        with self._lock:
            if indicator_code in self._indicator_cache:
                return self._indicator_cache[indicator_code]

        # The IMF code may differ from our indicator code
        imf_code = self.indicators[indicator_code].get("_imf_code", indicator_code)

        for attempt in range(MAX_RETRIES):
            try:
                self._respect_rate_limit()
                url = (
                    "https://www.imf.org/external/datamapper"
                    f"/api/v1/{imf_code}"
                )
                resp = self.session.get(url, timeout=REQUEST_TIMEOUT)
                resp.raise_for_status()
                body = resp.json()

                country_data = body.get("values", {}).get(imf_code, {})
                with self._lock:
                    self._indicator_cache[indicator_code] = country_data
                return country_data

            except requests.exceptions.RequestException as e:
                if attempt == MAX_RETRIES - 1:
                    print(f"Failed to fetch {indicator_code} (IMF {imf_code}): {e}")
                else:
                    time.sleep(1)

        return {}

    def fetch_indicator(self, indicator_code, group_code, countries):
        """Fetch IMF indicator data, filtered to group countries."""
        # Build ISO3 lookup for this group
        group_iso3s = {}
        for country in countries:
            group_iso3s[country["ISO3"]] = country

        if not group_iso3s:
            return None

        # Fetch all data (cached across groups)
        all_data = self._fetch_all_indicator_data(indicator_code)
        if not all_data:
            return None

        records = []
        for iso3, country in group_iso3s.items():
            year_data = all_data.get(iso3, {})
            for year_str, value in year_data.items():
                if value is None:
                    continue

                try:
                    value = float(value)
                except (ValueError, TypeError):
                    continue

                year_int = int(year_str[:4])
                if year_int < 2010 or year_int > 2030:
                    continue

                records.append({
                    "indicator": {
                        "id": indicator_code,
                        "value": self.indicators[indicator_code]["description"],
                    },
                    "country": {
                        "id": country["ISO"],
                        "value": country["name"],
                    },
                    "countryiso3code": iso3,
                    "date": str(year_int),
                    "value": value,
                    "unit": "",
                    "obs_status": "",
                    "decimal": 0,
                })

        if not records:
            return None

        metadata = {
            "page": 1,
            "pages": 1,
            "per_page": 10000,
            "total": len(records),
            "sourceid": "IMF",
            "lastupdated": "",
        }
        return [metadata, records]
