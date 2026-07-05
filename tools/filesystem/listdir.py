from pathlib import Path


def list_directory() -> str:
    cwd = Path.cwd()

    items = sorted(cwd.iterdir())

    if not items:
        return "Directory is empty."

    output = ["Directory Contents\n"]

    for item in items:
        icon = "📁" if item.is_dir() else "📄"
        output.append(f"{icon} {item.name}")

    return "\n".join(output)