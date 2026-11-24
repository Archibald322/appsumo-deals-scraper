"""
AppSumo Lifetime Deals & Software Scraper - Client Runner
Calls the canonical Apify Actor 'moneygain/appsumo-deals-scraper' via Pay-Per-Event API.
"""

import os
import json
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

APIFY_TOKEN = os.getenv("APIFY_TOKEN")
if not APIFY_TOKEN:
    raise ValueError("Missing APIFY_TOKEN in environment or .env file.")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "queries": ["ai", "lead-generation"],
    "minDiscount": 70,
    "maxItems": 10,
}

print(f"🚀 Calling moneygain/appsumo-deals-scraper with input: {json.dumps(run_input)}")
run = client.actor("moneygain/appsumo-deals-scraper").call(run_input=run_input)

print(f"✅ Actor run completed! Status: {run['status']}. Dataset ID: {run['defaultDatasetId']}")
dataset = client.dataset(run["defaultDatasetId"])

items = dataset.list_items().items
print(f"📊 Downloaded {len(items)} AppSumo software deals:")
for item in items[:5]:
    print(f" - {item.get('name')} (${item.get('price')} / ~${item.get('originalPrice')}, {item.get('discountPercentage')}% OFF) [{item.get('category')}]: {item.get('productUrl')}")
