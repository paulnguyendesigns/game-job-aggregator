import requests
import logging
from datetime import datetime
from src.models.job import Job, Source

logger = logging.getLogger(__name__)


def fetch_jobs(site_slug: str, company_name: str) -> list[Job]:
    """Fetch and parse all jobs from a company's Lever board.

    If one job fails to parse, log it and skip it — don't crash the whole batch.
    """
    raw_jobs = fetch_raw_jobs(site_slug)
    jobs = []

    for raw in raw_jobs:
        try:
            job = parse_job(raw, company_name=company_name)
            jobs.append(job)
        except Exception as e:
            logger.warning("Skipping malformed job from %s: %s", site_slug, e)

    return jobs

def fetch_raw_jobs(site_slug: str) -> list[dict]:
    """Fetch the raw job list from a company's public Lever board."""
    url = f"https://api.lever.co/v0/postings/{site_slug}?mode=json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def parse_job(raw: dict, company_name: str) -> Job:
    """Convert one raw Lever job dict into our normalized Job model."""
    posted_at = datetime.fromtimestamp(raw["createdAt"] / 1000)

    return Job(
        company=company_name,
        role=raw["text"],
        application_url=raw["hostedUrl"],
        source=Source.LEVER,
        location=raw["categories"]["location"],
        date_posted=posted_at.date(),
    )