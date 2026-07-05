from pathlib import Path


def create_file(filename: str) -> str:
    filename = filename.strip()

    if not filename:
        return "Please specify a file name."

    path = (Path.cwd() / filename).resolve()
    workspace = Path.cwd().resolve()

    if workspace not in path.parents:
        return "Access denied."

    if path.exists():
        return "File already exists."

    try:
        path.touch()

        return (
            "File created successfully.\n\n"
            f"{path.name}"
        )

    except Exception as e:
        return f"Error creating file: {e}"