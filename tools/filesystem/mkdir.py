from pathlib import Path


def create_folder(foldername: str) -> str:
    foldername = foldername.strip()

    if not foldername:
        return "Please specify a folder name."

    path = (Path.cwd() / foldername).resolve()
    workspace = Path.cwd().resolve()

    if workspace not in path.parents:
        return "Access denied."

    if path.exists():
        return "Folder already exists."

    try:
        path.mkdir(parents=True)

        return (
            "Folder created successfully.\n\n"
            f"{path.name}"
        )

    except Exception as e:
        return f"Error creating folder: {e}"