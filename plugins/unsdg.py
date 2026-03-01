"""UN SDG Global Database plugin.

API: https://unstats.un.org/sdgs/UNSDGAPIV5/v1/sdg/Series/Data
Fetches all data for a series in bulk, then filters by group countries.
Uses M49 numeric country codes for matching.
"""

import time
import threading
import requests
from plugins.base import DataSourcePlugin
from plugins.country_mapping import build_iso3_to_m49_map, build_m49_to_iso_map

MAX_RETRIES = 3
RATE_LIMIT_DELAY = 0.3
REQUEST_TIMEOUT = 60
PAGE_SIZE = 10000


class UNSDGPlugin(DataSourcePlugin):
    SOURCE_NAME = "UN SDG"
    SOURCE_URL = "https://unstats.un.org/sdgs/dataportal"
    SOURCE_DB = "UN SDG Global Database"

    def __init__(self, indicators_dict, **kwargs):
        super().__init__(indicators_dict, **kwargs)
        self.session = requests.Session()
        self.iso3_to_m49 = build_iso3_to_m49_map()
        self.m49_to_iso = build_m49_to_iso_map()
        self.last_request_time = 0
        self._lock = threading.Lock()
        # Cache of raw series data: {indicator_code: [all_records]}
        self._series_cache = {}

    def _respect_rate_limit(self):
        with self._lock:
            elapsed = time.time() - self.last_request_time
            if elapsed < RATE_LIMIT_DELAY:
                time.sleep(RATE_LIMIT_DELAY - elapsed)
            self.last_request_time = time.time()

    def _fetch_all_series_data(self, indicator_code):
        """Fetch all data points for a series (all countries, all years)."""
        with self._lock:
            if indicator_code in self._series_cache:
                return self._series_cache[indicator_code]

        all_data = []
        page = 1

        while True:
            for attempt in range(MAX_RETRIES):
                try:
                    self._respect_rate_limit()
                    url = (
                        "https://unstats.un.org/sdgs/UNSDGAPIV5"
                        f"/v1/sdg/Series/Data"
                        f"?seriesCode={indicator_code}"
                        f"&pageSize={PAGE_SIZE}&page={page}"
                    )
                    resp = self.session.get(url, timeout=REQUEST_TIMEOUT)
                    resp.raise_for_status()
                    body = resp.json()

                    data_points = body.get("data", [])
                    all_data.extend(data_points)

                    total_pages = body.get("totalPages", 1)
                    break  # success

                except requests.exceptions.RequestException as e:
                    if attempt == MAX_RETRIES - 1:
                        print(f"Failed to fetch {indicator_code} page {page}: {e}")
                        self._series_cache[indicator_code] = all_data
                        return all_data
                    time.sleep(1)
            else:
                break

            if page >= total_pages:
                break
            page += 1

        self._series_cache[indicator_code] = all_data
        return all_data

    def fetch_indicator(self, indicator_code, group_code, countries):
        """Fetch SDG series data, filtered to group countries."""
        # Build set of M49 codes for this group
        group_m49s = set()
        m49_to_country = {}
        for country in countries:
            m49 = self.iso3_to_m49.get(country["ISO3"])
            if m49 is not None:
                group_m49s.add(str(m49))
                m49_to_country[str(m49)] = country

        if not group_m49s:
            return None

        # Fetch all data for this series (cached across groups)
        all_data = self._fetch_all_series_data(indicator_code)

        # Filter to group countries and normalize
        records = []
        seen = set()  # (m49, year) dedup

        for dp in all_data:
            area_code = str(dp.get("geoAreaCode", ""))
            if area_code not in group_m49s:
                continue

            year = str(dp.get("timePeriodStart", dp.get("year", "")))
            value = dp.get("value")
            if value is None or year == "":
                continue

            try:
                value = float(value)
            except (ValueError, TypeError):
                continue

            year_int = int(year[:4])
            if year_int < 2010 or year_int > 2025:
                continue

            key = (area_code, year_int)
            if key in seen:
                continue
            seen.add(key)

            m49_int = int(area_code)
            iso_info = self.m49_to_iso.get(m49_int, {})
            country = m49_to_country.get(area_code, {})

            records.append({
                "indicator": {
                    "id": indicator_code,
                    "value": self.indicators[indicator_code]["description"],
                },
                "country": {
                    "id": iso_info.get("iso2", country.get("ISO", "")),
                    "value": iso_info.get("name", country.get("name", "")),
                },
                "countryiso3code": iso_info.get("iso3", country.get("ISO3", "")),
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
            "sourceid": "UN SDG",
            "lastupdated": "",
        }
        return [metadata, records]
