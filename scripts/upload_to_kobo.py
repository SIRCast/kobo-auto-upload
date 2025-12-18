import os
import pandas as pd
import requests
import json

KOBO_URL = "https://kf.kobotoolbox.org"
API_TOKEN = os.getenv("KOBO_TOKEN")
ASSET_ID = os.getenv("KOBO_ASSET_ID")

endpoint = f"{KOBO_URL}/api/v2/assets/{ASSET_ID}/data/"

headers = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json"
}

df = pd.read_csv("data/data.csv")

for i, row in df.iterrows():
    payload = row.dropna().to_dict()
    r = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    print(f"Row {i+1}: {r.status_code}")
