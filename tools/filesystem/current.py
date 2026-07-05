from pathlib import Path


def current_directory() -> str:
    cwd = Path.cwd()

    return (
        "Current Directory\n\n"
        f"{cwd}"
    )