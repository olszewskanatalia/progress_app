import re


def are_valid_episodes(episodes):
    pattern = r"^E\d+$"
    for e in episodes:
        if not re.match(pattern, e):
            return False
    return True
