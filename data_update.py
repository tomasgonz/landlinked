from indicators import WorldBankAPI, indicators

# Initialize the API client
api_client = WorldBankAPI(indicators)

# List of groups to process
groups = ["lldcs", "ldcs", "sids", "g77", "brics", "eu"]

# Process each group
for group_code in groups:
    print(f"\n===== Processing group: {group_code} =====")
    api_client.download_all_indicators(group_code)
    print(f"===== Completed group: {group_code} =====\n")

print("All indicator data downloads completed successfully!")
