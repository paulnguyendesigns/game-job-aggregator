GAME_KEYWORDS = [
    "game", "gameplay", "game development", "game engine",
    "unity", "unreal", "unreal engine", "godot",
    "level design", "game design", "game studio",
    "interactive entertainment", "player experience",
]


def is_game_relevant(job) -> bool:
    """Check whether a job's title suggests it's actually game-related,
    for use with companies that make games alongside other products."""
    text = job.role.lower()

    for keyword in GAME_KEYWORDS:
        if keyword in text:
            return True

    return False