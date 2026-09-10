import requests


def fetch_raw_jobs(site_slug: str) -> list[dict]:
    """Fetch the raw job list from a company's public Lever board."""
    url = f"https://api.lever.co/v0/postings/{site_slug}?mode=json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()