from pathlib import Path
import shutil


def move_file(source: str, destination: str) -> str:
    source = source.strip()
    destination = destination.strip()

    if not source or not destination:
        return "Please specify both source and destination."

    workspace = Path.cwd().resolve()

    source_path = (workspace / source).resolve()
    destination_path = (workspace / destination).resolve()

    if workspace not in source_path.parents:
        return "Access denied."

    if workspace not in destination_path.parents:
        return "Access denied."

    if not source_path.exists():
        return "File not found."

    # Destination is an existing folder
    if destination_path.exists() and destination_path.is_dir():
        destination_path = destination_path / source_path.name

    if destination_path.exists():
        return "Destination already exists."

    if source_path.is_dir():
        return "Moving directories is not supported."

    try:
        shutil.move(
            str(source_path),
            str(destination_path),
        )

        return (
            "File moved successfully.\n\n"
            f"{source_path.name} → {destination_path}"
        )

    except Exception as e:
        return f"Error moving file: {e}"