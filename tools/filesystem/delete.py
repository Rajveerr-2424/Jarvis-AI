from pathlib import Path


def delete_file(filename: str) -> str:
    filename = filename.strip()

    if not filename:
        return "Please specify a file."

    workspace = Path.cwd().resolve()

    path = (workspace / filename).resolve()

    if workspace not in path.parents:
        return "Access denied."

    if not path.exists():
        return "File not found."

    if path.is_dir():
        return "Cannot delete a directory."

    try:
        path.unlink()

        return (
            "File deleted successfully.\n\n"
            f"{path.name}"
        )

    except Exception as e:
        return f"Error deleting file: {e}"