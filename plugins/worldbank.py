"""World Bank data source plugin.

Wraps the existing World Bank API v2 fetch logic. The API response
is already in the normalized [metadata, records[]] format, so no
transformation is needed.
"""

import time
import requests
import concurrent.futures
from plugins.base import DataSourcePlugin

API_RATE_LIMIT_DELAY = 0.5
MAX_RETRIES = 3


class WorldBankPlugin(DataSourcePlugin):
    SOURCE_NAME = "World Bank"
    SOURCE_URL = "https://data.worldbank.org"
    SOURCE_DB = "World Development Indicators"

    def __init__(self, indicators_dict, **kwargs):
        super().__init__(indicators_dict, **kwargs)
        self.session = requests.Session()
        self.last_request_time = 0

    def _respect_rate_limit(self):
        elapsed = time.time() - self.last_request_time
        if elapsed < API_RATE_LIMIT_DELAY:
            time.sleep(API_RATE_LIMIT_DELAY - elapsed)
        self.last_request_time = time.time()

    def _fetch_page(self, indicator_code, countries_str, page):
        try:
            self._respect_rate_limit()
            url = (
                f"https://api.worldbank.org/v2/country/{countries_str}"
                f"/indicator/{indicator_code}"
                f"?date=2010:2025&format=json&per_page=10000&page={page}"
            )
            resp = self.session.get(url, timeout=10)
            resp.raise_for_status()
            return resp.json()[1]
        except Exception as e:
            print(f"Error fetching page {page} for {indicator_code}: {e}")
            return []

    def fetch_indicator(self, indicator_code, group_code, countries):
        """Fetch from World Bank API v2, joining country ISO2 codes with ';'."""
        countries_str = ";".join(c["ISO"] for c in countries)

        for attempt in range(MAX_RETRIES):
            try:
                self._respect_rate_limit()
                url = (
                    f"https://api.worldbank.org/v2/country/{countries_str}"
                    f"/indicator/{indicator_code}"
                    f"?date=2010:2025&per_page=10000&format=json"
                )
                resp = self.session.get(url, timeout=10)
                resp.raise_for_status()
                result = resp.json()

                if not result or len(result) < 2:
                    return None

                metadata, first_page = result
                data = first_page

                # Handle pagination
                if "pages" in metadata and metadata["pages"] > 1:
                    pages = metadata["pages"]
                    with concurrent.futures.ThreadPoolExecutor(
                        max_workers=min(pages - 1, 4)
                    ) as executor:
                        futures = {
                            executor.submit(
                                self._fetch_page, indicator_code, countries_str, p
                            ): p
                            for p in range(2, pages + 1)
                        }
                        for future in concurrent.futures.as_completed(futures):
                            page_data = future.result()
                            if page_data:
                                data.extend(page_data)

                return [metadata, data]

            except requests.exceptions.RequestException as e:
                if attempt == MAX_RETRIES - 1:
                    print(
                        f"Failed to fetch {indicator_code} after "
                        f"{MAX_RETRIES} attempts: {e}"
                    )
                    return None
                time.sleep(1)

        return None
