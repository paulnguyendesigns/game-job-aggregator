import requests
import logging
from datetime import datetime
from src.models.job import Job, Source

logger = logging.getLogger(__name__)

def fetch_raw_jobs(board_token: str) -> list[dict]:
    """Fetch the raw job list from a company's public Greenhouse board."""
    url = f"https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["jobs"]

def fetch_jobs(board_token: str) -> list[Job]:
    """Fetch and parse all jobs from a company's Greenhouse board.

    If one job fails to parse, log it and skip it — don't crash the whole batch.
    """
    raw_jobs = fetch_raw_jobs(board_token)
    jobs = []

    for raw in raw_jobs:
        try:
            job = parse_job(raw)
            jobs.append(job)
        except Exception as e:
            logger.warning("Skipping malformed job from %s: %s", board_token, e)

    return jobs

def parse_job(raw: dict) -> Job:
    """Convert one raw Greenhouse job dict into our normalized Job model."""
    posted_at = datetime.fromisoformat(raw["first_published"])

    return Job(
        company=raw["company_name"],
        role=raw["title"],
        application_url=raw["absolute_url"],
        source=Source.GREENHOUSE,
        location=raw["location"]["name"],
        date_posted=posted_at.date(),
    )