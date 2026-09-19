from src.companies import COMPANIES
from src.sources import greenhouse, lever, ashby
import argparse

def fetch_all_jobs():
    """Fetch jobs from every company in COMPANIES, using the right adapter for each."""
    all_jobs = []

    for company in COMPANIES:
        name = company["name"]
        source = company["source"]
        identifier = company["identifier"]

        if source == "greenhouse":
            jobs = greenhouse.fetch_jobs(identifier)
        elif source == "lever":
            jobs = lever.fetch_jobs(identifier, company_name=name)
        elif source == "ashby":
            jobs = ashby.fetch_jobs(identifier, company_name=name)
        else:
            print(f"Unknown source '{source}' for {name}, skipping")
            continue

        print(f"{name}: found {len(jobs)} jobs")
        all_jobs.extend(jobs)

    return all_jobs

def main():
    parser = argparse.ArgumentParser(description="Aggregate game development internship listings.")
    parser.add_argument("--verbose", action="store_true", help="Show more detailed output.")
    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode is ON")
    print("game-job-aggregator — starting up")


if __name__ == "__main__":
    main()