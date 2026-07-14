from pathlib import Path


def append_file(filename: str, content: str) -> str:
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
        return "Cannot append to a directory."

    try:
        with path.open(
            "a",
            encoding="utf-8",
        ) as file:

            # Insert a newline only if the file already contains data.
            if path.stat().st_size > 0:
                file.write("\n")

            file.write(content)

        return (
            "Content appended successfully.\n\n"
            f"{path.name}"
        )

    except Exception as e:
        return f"Error appending file: {e}"