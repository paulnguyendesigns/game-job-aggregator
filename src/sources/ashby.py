import requests
import logging
from datetime import datetime
from src.models.job import Job, Source

logger = logging.getLogger(__name__)

def fetch_raw_jobs(job_board_name: str) -> list[dict]:
    """Fetch the raw job list from a company's public Ashby board."""
    url = f"https://api.ashbyhq.com/posting-api/job-board/{job_board_name}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["jobs"]

def fetch_jobs(job_board_name: str, company_name: str) -> list[Job]:
    """Fetch and parse all jobs from a company's Ashby board.

    If one job fails to parse, log it and skip it — don't crash the whole batch.
    """
    raw_jobs = fetch_raw_jobs(job_board_name)
    jobs = []

    for raw in raw_jobs:
        try:
            job = parse_job(raw, company_name=company_name)
            jobs.append(job)
        except Exception as e:
            logger.warning("Skipping malformed job from %s: %s", job_board_name, e)

    return jobs

def parse_job(raw: dict, company_name: str) -> Job:
    """Convert one raw Ashby job dict into our normalized Job model."""
    posted_at = datetime.fromisoformat(raw["publishedAt"].replace("Z", "+00:00"))

    return Job(
        company=company_name,
        role=raw["title"],
        application_url=raw["jobUrl"],
        source=Source.ASHBY,
        location=raw["location"],
        remote=raw.get("isRemote", False),
        date_posted=posted_at.date(),
    )