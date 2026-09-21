INTERNSHIP_KEYWORDS = ["intern", "internship", "co-op", "coop"]


def is_internship(job) -> bool:
    """Check whether a job's title suggests it's an internship or co-op."""
    title = job.role.lower()

    for keyword in INTERNSHIP_KEYWORDS:
        if keyword in title:
            return True

    return False