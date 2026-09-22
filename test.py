from src.main import fetch_all_jobs
from src.processing.filters import is_internship
from src.output.writer import write_markdown

all_jobs = fetch_all_jobs()
internships = [job for job in all_jobs if is_internship(job)]

write_markdown(internships)
print("Wrote jobs.md")