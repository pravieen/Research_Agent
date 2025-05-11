# tools/semantic_scholar_api.py
import requests
from typing import List, Dict
from src.utils.cache import get_cache_key, get_cached_result, save_to_cache

def search_semantic_scholar(query: str, max_results: int = 5) -> List[Dict]:
    cache_key = get_cache_key(f"ss_{query}", max_results)
    cached = get_cached_result(cache_key)
    if cached:
        print("Returning cached Semantic Scholar results")
        return cached

    url = "https://api.semanticscholar.org/graph/v1/paper/search "
    headers = {"x-api-key": "YOUR_API_KEY_HERE"}
    params = {
        "query": query,
        "limit": max_results,
        "fields": "title,abstract,url,year,authors,citationCount"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch from Semantic Scholar: {response.status_code} - {response.text}")

    data = response.json()
    papers = data.get("data", [])

    save_to_cache(cache_key, papers)

    return papers