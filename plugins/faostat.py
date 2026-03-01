"""FAOSTAT data source plugin.

API: https://fenixservices.fao.org/faostat/api/v1/en/data/{domain}
Uses M49 numeric country codes. Batch-fetches all countries at once
(API accepts comma-separated M49 area codes).

Indicator codes follow the pattern FAO.{DOMAIN}.{SHORT}, and each
indicator's metadata must include a '_fao_params' dict with keys
'domain', 'item', 'element'.
"""

import time
import requests
from plugins.base import DataSourcePlugin
from plugins.country_mapping import build_iso3_to_m49_map, build_m49_to_iso_map

MAX_RETRIES = 3
RATE_LIMIT_DELAY = 0.5
YEARS = ",".join(str(y) for y in range(2010, 2026))


class FAOSTATPlugin(DataSourcePlugin):
    SOURCE_NAME = "FAOSTAT"
    SOURCE_URL = "https://www.fao.org/faostat"
    SOURCE_DB = "FAOSTAT"

    def __init__(self, indicators_dict, **kwargs):
        super().__init__(indicators_dict, **kwargs)
        self.session = requests.Session()
        self.iso3_to_m49 = build_iso3_to_m49_map()
        self.m49_to_iso = build_m49_to_iso_map()
        self.last_request_time = 0

    def _respect_rate_limit(self):
        elapsed = time.time() - self.last_request_time
        if elapsed < RATE_LIMIT_DELAY:
            time.sleep(RATE_LIMIT_DELAY - elapsed)
        self.last_request_time = time.time()

    def _clean_m49(self, raw):
        """Strip FAOSTAT's apostrophe-prefix quirk from M49 codes."""
        s = str(raw).strip().lstrip("'")
        try:
            return int(s)
        except ValueError:
            return None

    def fetch_indicator(self, indicator_code, group_code, countries):
        """Fetch from FAOSTAT API using _fao_params metadata."""
        meta = self.indicators.get(indicator_code)
        if not meta:
            return None

        fao_params = meta.get("_fao_params")
        if not fao_params:
            print(f"[FAOSTAT] No _fao_params for {indicator_code}")
            return None

        domain = fao_params["domain"]
        item = fao_params["item"]
        element = fao_params["element"]

        # Build comma-separated M49 area codes
        m49_codes = []
        for c in countries:
            m49 = self.iso3_to_m49.get(c["ISO3"])
            if m49 is not None:
                m49_codes.append(str(m49))

        if not m49_codes:
            return None

        area_str = ",".join(m49_codes)

        for attempt in range(MAX_RETRIES):
            try:
                self._respect_rate_limit()
                url = (
                    f"https://fenixservices.fao.org/faostat/api/v1/en/data/{domain}"
                    f"?area={area_str}&element={element}&item={item}"
                    f"&year={YEARS}"
                )
                resp = self.session.get(url, timeout=30)
                resp.raise_for_status()
                body = resp.json()

                data_points = body.get("data", [])
                records = []

                for dp in data_points:
                    year = str(dp.get("Year", ""))
                    value = dp.get("Value")
                    if value is None or year == "":
                        continue

                    try:
                        value = float(value)
                    except (ValueError, TypeError):
                        continue

                    raw_area = dp.get("Area Code (M49)", dp.get("Area Code", ""))
                    m49 = self._clean_m49(raw_area)
                    if m49 is None:
                        continue

                    iso_info = self.m49_to_iso.get(m49, {})
                    if not iso_info:
                        continue

                    records.append({
                        "indicator": {
                            "id": indicator_code,
                            "value": meta["description"],
                        },
                        "country": {
                            "id": iso_info["iso2"],
                            "value": iso_info["name"],
                        },
                        "countryiso3code": iso_info["iso3"],
                        "date": year[:4],
                        "value": value,
                        "unit": dp.get("Unit", ""),
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
                    "sourceid": "FAOSTAT",
                    "lastupdated": "",
                }
                return [metadata, records]

            except requests.exceptions.RequestException as e:
                if attempt == MAX_RETRIES - 1:
                    print(f"Failed to fetch {indicator_code} after {MAX_RETRIES} attempts: {e}")
                    return None
                time.sleep(1)

        return None
