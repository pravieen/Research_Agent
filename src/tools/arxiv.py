# tools/arxiv_api.py
import feedparser
import requests
from typing import List, Dict
from src.utils.cache import get_cached_result, save_to_cache, get_cache_key


def search_arxiv(query: str, max_results: int = 5) -> List[Dict]:
    cache_key = get_cache_key(query, max_results)

    # Check cache first
    cached = get_cached_result(cache_key)
    if cached:
        print("Returning cached results")
        return cached

    base_url = 'http://export.arxiv.org/api/query'
    params = {
        'search_query': f'all:{query}',
        'start': 0,
        'max_results': max_results
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch papers: {response.status_code} - {response.reason}")

    feed = feedparser.parse(response.text)

    papers = []
    for entry in feed.entries:
        papers.append({
            "title": entry.title.strip(),
            "summary": entry.summary.strip(),
            "url": entry.link,
            "pdf_url": entry.link.replace('/abs/', '/pdf/'),  # arXiv PDF link
            "published": entry.published,
            "authors": [author.name for author in entry.authors]
        })

    # Save to cache
    save_to_cache(cache_key, papers)
    print(papers)
    return papers