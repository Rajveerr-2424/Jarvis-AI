from pathlib import Path


def write_file(filename: str, content: str) -> str:
    filename = filename.strip()

    if not filename:
        return "Please specify a file."

    path = (Path.cwd() / filename).resolve()
    workspace = Path.cwd().resolve()

    if workspace not in path.parents:
        return "Access denied."

    if not path.exists():
        return "File not found."

    if path.is_dir():
        return "Cannot write to a directory."

    try:
        path.write_text(
            content,
            encoding="utf-8",
        )

        return (
            "File written successfully.\n\n"
            f"{path.name}"
        )

    except Exception as e:
        return f"Error writing file: {e}"