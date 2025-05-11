# utils/cache.py
import os
import json
from datetime import datetime, timedelta

CACHE_DIR = ".cache/arxiv"
CACHE_TTL = timedelta(hours=24)  # Cache paper results for 24 hours

os.makedirs(CACHE_DIR, exist_ok=True)

def get_cache_key(query: str, max_results: int):
    safe_query = "".join(c if c.isalnum() else "_" for c in query)
    return f"{safe_query}_{max_results}.json"

def get_cached_result(cache_key: str):
    cache_path = os.path.join(CACHE_DIR, cache_key)
    if not os.path.exists(cache_path):
        return None

    with open(cache_path, "r") as f:
        data = json.load(f)

    # Check TTL
    timestamp = datetime.fromisoformat(data["timestamp"])
    if datetime.now() - timestamp > CACHE_TTL:
        return None

    return data["papers"]

def save_to_cache(cache_key: str, papers: list):
    cache_path = os.path.join(CACHE_DIR, cache_key)
    data = {
        "timestamp": datetime.now().isoformat(),
        "papers": papers
    }
    with open(cache_path, "w") as f:
        json.dump(data, f, indent=2)