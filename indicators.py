import requests
import pandas as pd
import datetime
import os
import json
from groups import get_group_countries_iso3
from time import sleep
from indicators_data import indicators

CACHE_DIR = './cache/indicators'

def get_indicator(indicator_code, group_code):
    indicator = indicators.get(indicator_code)
    if indicator is not None:
        if indicator['source'] == 'World Bank':
            return get_world_bank_data(indicator_code, group_code)
        else:
            return None
    else:
        print("Indicator not found in list.")
        return None

def download_indicators_data(group_code):
    for indicator_code in indicators:
        get_indicator(indicator_code, group_code)

def get_world_bank_data(indicator_code, group_code):
    group = [country_code for country_code in get_group_countries_iso3(group_code)]
    countries = ';'.join(group)
    indicator = indicators.get(indicator_code)
    print(indicator_code)
    if indicator is not None:
        cache_file = os.path.join(CACHE_DIR, f"{indicator_code}_{group_code}.json")  # Modify cache file name based on indicator code and group
        if os.path.exists(cache_file):
            # Check if the cache file is older than a month
            cache_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(cache_file))
            current_time = datetime.datetime.now()
            if (current_time - cache_modified_time).days <= 30:
                # Read the data from the cache file
                with open(cache_file, 'r') as file:
                    data = json.load(file)
                print("Data found in cache. Returning data.")
                return data

        # Fetch data from the World Bank API for group countries only
        url = f"https://api.worldbank.org/v2/country/{countries}/indicator/{indicator_code}?date=2010:2024&per_page=10000&format=json"
        print("Request sent to %s" % url)
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Data fetched from the World Bank API.")
            # Check if there are more pages of data
            if 'pages' in data[0] and data[0]['pages'] > 1:
                pages = data[0]['pages']
                print("fetching data from %d pages" % pages)
                if pages > 1:
                    # Fetch data from all pages
                    for page in range(2, pages + 1):
                        url = f"https://api.worldbank.org/v2/country/{countries}/indicator/{indicator_code}?date=2010:2024&format=json&per_page=10000&page={page}"
                        response = requests.get(url)
                        if response.status_code == 200:
                            page_data = response.json()
                            data[1].extend(page_data[1])
                        else:
                            print(f"Failed to fetch data from page {page} of the World Bank API.")
            # Save the data to the cache file
            print("Saving data to cache file.")
            with open(cache_file, 'w') as file:
                json.dump(data, file)
            return data
        else:
            print("Data saved to cache file. Returning data.")
            return None

def download_all_indicators(group_code):
    for indicator_code in indicators:
        sleep(5) # Sleep for 20 seconds between requests to avoid hitting the API rate limit
        get_indicator(indicator_code, group_code)

def load_indicator_country_data_from_cache(indicator_code, group_code, country_name):
    cache_file = os.path.join(CACHE_DIR, f"{indicator_code}_{group_code}.json")
    country_data = []
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as file:
            data = json.load(file)
            for item in data[1]:
                if item['country']['value'] == country_name:
                    country_data.append(item)
            return country_data

    return None
