import requests
import pandas as pd
import datetime
import os
import json
import concurrent.futures
from functools import lru_cache
from groups import get_group_countries_iso3
import time
from indicators_data import indicators

# Configuration
CACHE_DIR = './cache/indicators'
CACHE_DURATION_DAYS = 30
MAX_WORKERS = 8  # Adjust based on CPU cores and rate limits
API_RATE_LIMIT_DELAY = 0.5  # Reduced from 5 seconds
MAX_RETRIES = 3
BATCH_SIZE = 20  # Process indicators in batches to control memory usage

# Ensure cache directory exists
os.makedirs(CACHE_DIR, exist_ok=True)

class WorldBankAPI:
    """Class to handle World Bank API interactions with efficient caching and rate limiting"""

    def __init__(self, indicators_dict):
        self.indicators = indicators_dict
        self.session = requests.Session()  # Reuse session for connection pooling
        self.last_request_time = 0

    def _respect_rate_limit(self):
        """Simple rate limiter to avoid hitting API limits"""
        elapsed = time.time() - self.last_request_time
        if elapsed < API_RATE_LIMIT_DELAY:
            time.sleep(API_RATE_LIMIT_DELAY - elapsed)
        self.last_request_time = time.time()

    def _get_cache_path(self, indicator_code, group_code):
        """Generate cache file path"""
        return os.path.join(CACHE_DIR, f"{indicator_code}_{group_code}.json")

    def _is_cache_valid(self, cache_path):
        """Check if cache is still valid based on age"""
        if not os.path.exists(cache_path):
            return False

        cache_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(cache_path))
        current_time = datetime.datetime.now()
        return (current_time - cache_modified_time).days <= CACHE_DURATION_DAYS

    def _fetch_from_api(self, indicator_code, countries_str):
        """Fetch data from World Bank API with retries"""
        data = []

        # First request to get metadata and first page
        for attempt in range(MAX_RETRIES):
            try:
                self._respect_rate_limit()
                url = f"https://api.worldbank.org/v2/country/{countries_str}/indicator/{indicator_code}?date=2010:2025&per_page=10000&format=json"
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                result = response.json()

                if not result or len(result) < 2:
                    return None  # No data available

                metadata, first_page = result
                data = first_page

                # Handle pagination efficiently
                if 'pages' in metadata and metadata['pages'] > 1:
                    pages = metadata['pages']

                    # Use a thread pool for parallel page requests
                    with concurrent.futures.ThreadPoolExecutor(max_workers=min(pages-1, 4)) as executor:
                        future_to_page = {
                            executor.submit(
                                self._fetch_page,
                                indicator_code,
                                countries_str,
                                page
                            ): page
                            for page in range(2, pages + 1)
                        }

                        for future in concurrent.futures.as_completed(future_to_page):
                            page_data = future.result()
                            if page_data:
                                data.extend(page_data)

                return [metadata, data]

            except requests.exceptions.RequestException as e:
                if attempt == MAX_RETRIES - 1:
                    print(f"Failed to fetch data for {indicator_code} after {MAX_RETRIES} attempts: {e}")
                    return None
                time.sleep(1)  # Wait before retry

        return None

    def _fetch_page(self, indicator_code, countries_str, page):
        """Helper to fetch a specific page of results"""
        try:
            self._respect_rate_limit()
            url = f"https://api.worldbank.org/v2/country/{countries_str}/indicator/{indicator_code}?date=2010:2025&format=json&per_page=10000&page={page}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.json()[1]  # Return just the data part
        except Exception as e:
            print(f"Error fetching page {page} for {indicator_code}: {e}")
            return []

    @lru_cache(maxsize=32)
    def get_group_countries(self, group_code):
        """Cache group country codes to avoid repeated lookups"""
        return [country_code for country_code in get_group_countries_iso3(group_code)]

    def get_indicator(self, indicator_code, group_code):
        """Get indicator data with efficient caching"""
        # Check if this is a supported indicator
        if indicator_code not in self.indicators:
            print(f"Indicator {indicator_code} not found in list.")
            return None

        indicator = self.indicators[indicator_code]
        if indicator['source'] != 'World Bank':
            print(f"Indicator {indicator_code} is not from World Bank.")
            return None

        # Check cache
        cache_path = self._get_cache_path(indicator_code, group_code)
        if self._is_cache_valid(cache_path):
            with open(cache_path, 'r') as file:
                return json.load(file)

        # Prepare request
        countries = self.get_group_countries(group_code)
        countries_str = ';'.join(countries)

        # Fetch from API
        print(f"Fetching {indicator_code} for group {group_code}")
        data = self._fetch_from_api(indicator_code, countries_str)

        if data:
            # Save to cache
            with open(cache_path, 'w') as file:
                json.dump(data, file)
            return data

        return None

    def download_all_indicators(self, group_code):
        """Download all indicators efficiently using batched processing"""
        indicator_codes = list(self.indicators.keys())

        # Process in batches to control memory usage
        for i in range(0, len(indicator_codes), BATCH_SIZE):
            batch = indicator_codes[i:i+BATCH_SIZE]

            with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                # Map indicator codes to download tasks
                future_to_indicator = {
                    executor.submit(self.get_indicator, code, group_code): code
                    for code in batch
                }

                # Process results as they complete
                for future in concurrent.futures.as_completed(future_to_indicator):
                    indicator = future_to_indicator[future]
                    try:
                        result = future.result()
                        if result:
                            print(f"✓ Successfully fetched {indicator}")
                        else:
                            print(f"✗ Failed to fetch {indicator}")
                    except Exception as e:
                        print(f"! Error processing {indicator}: {e}")

def load_indicator_country_data_from_cache(indicator_code, group_code, country_name):
    """Load country-specific data from cache with error handling"""
    cache_file = os.path.join(CACHE_DIR, f"{indicator_code}_{group_code}.json")

    try:
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as file:
                data = json.load(file)
                # Return only data for the specified country
                return [item for item in data[1] if item['country']['value'] == country_name]
        return None
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"Error loading data from cache for {indicator_code}, {country_name}: {e}")
        return None

# Initialize the API client
api_client = WorldBankAPI(indicators)

# Example usage:
def download_indicators_data(group_code):
    """Download all indicators for a group"""
    api_client.download_all_indicators(group_code)

def get_indicator(indicator_code, group_code):
    """Get a specific indicator for a group"""
    return api_client.get_indicator(indicator_code, group_code)
