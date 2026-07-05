from pathlib import Path


def read_file(filename: str) -> str:
    filename = filename.strip()

    if not filename:
        return "Please specify a file."

    path = Path.cwd() / filename

    try:
        path = path.resolve()
    except Exception:
        return "Invalid file path."

    workspace = Path.cwd().resolve()

    if workspace not in path.parents and path != workspace:
        return "Access denied."

    if not path.exists():
        return "File not found."

    if path.is_dir():
        return "Cannot read a directory."

    try:
        content = path.read_text(
            encoding="utf-8"
        )

    except UnicodeDecodeError:
        return "Only UTF-8 text files are supported."

    except Exception as e:
        return f"Error reading file: {e}"

    if not content.strip():
        return "File is empty."

    return (
        f"File: {path.name}\n\n"
        f"{content}"
    )