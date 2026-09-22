from datetime import date


def write_markdown(jobs, filepath="jobs.md"):
    """Write a list of Job objects out to a readable Markdown file,
    sorted by most recently posted first, then by company name."""

    sorted_jobs = sorted(
        jobs,
        key=lambda job: (-(job.date_posted or date.min).toordinal(), job.company),
    )

    lines = ["# 🎮 Game Development Internships", ""]

    for job in sorted_jobs:
        lines.append(f"### {job.company}")
        lines.append("")
        lines.append(f"**{job.role}**")
        lines.append("")
        lines.append(f"📍 {job.location}")
        lines.append("")
        lines.append(f"[Apply →]({job.application_url})")
        lines.append("")
        lines.append("---")
        lines.append("")

    content = "\n".join(lines)

    with open(filepath, "w") as f:
        f.write(content)