from pathlib import Path


def rename_file(old_name: str, new_name: str) -> str:
    old_name = old_name.strip()
    new_name = new_name.strip()

    if not old_name or not new_name:
        return "Please specify both source and destination names."

    workspace = Path.cwd().resolve()

    old_path = (workspace / old_name).resolve()
    new_path = (workspace / new_name).resolve()

    if workspace not in old_path.parents:
        return "Access denied."

    if workspace not in new_path.parents:
        return "Access denied."

    if not old_path.exists():
        return "File not found."

    if new_path.exists():
        return "Destination already exists."

    try:
        old_path.rename(new_path)

        return (
            "File renamed successfully.\n\n"
            f"{old_path.name} → {new_path.name}"
        )

    except Exception as e:
        return f"Error renaming file: {e}"