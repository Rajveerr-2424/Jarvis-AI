# Handles all file-related tool operations.

from click import argument

from tools.core.base import BaseTool

from tools.filesystem.append import append_file
from tools.filesystem.create import create_file
from tools.filesystem.current import current_directory
from tools.filesystem.listdir import list_directory
from tools.filesystem.read import read_file
from tools.filesystem.write import write_file
from tools.filesystem.mkdir import create_folder
from tools.filesystem.rename import rename_file
from tools.filesystem.copy import copy_file
from tools.filesystem.move import move_file
from tools.filesystem.delete import delete_file


class FileTool(BaseTool):
    name = "File"
    description = "File system operations."
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    keywords = (
        # Current Directory
        "current directory",
        "pwd",
        "where am i",

        # Directory Listing
        "list files",
        "show files",
        "dir",
        "ls",

        # Read File
        "read file",
        "rf",

        # Create File
        "create file",
        "cf",

        # Write File
        "write file",
        "wf",

        # Append File
        "append file",
        "af",

        # Folder
        "create folder",
        "mkdir",
        "md",

        # Rename File
        "rename file",
        "ren"

        # Copy File
        "copy file",
        "cp",

        # Move File
        "move file",
        "mv",

        # Delete File
        "delete file",
        "df",
    )

    def __init__(self):
        self.commands = {
            # --------------------------------------------------
            # Current Directory
            # --------------------------------------------------
            "current directory": self.current_directory,
            "pwd": self.current_directory,
            "where am i": self.current_directory,

            # --------------------------------------------------
            # Directory Listing
            # --------------------------------------------------
            "list files": self.list_directory,
            "show files": self.list_directory,
            "dir": self.list_directory,
            "ls": self.list_directory,

            # --------------------------------------------------
            # Read File
            # --------------------------------------------------
            "read file": self.read,
            "rf": self.read,

            # --------------------------------------------------
            # Create File
            # --------------------------------------------------
            "create file": self.create,
            "cf": self.create,

            # --------------------------------------------------
            # Write File
            # --------------------------------------------------
            "write file": self.write,
            "wf": self.write,

            # --------------------------------------------------
            # Append File
            # --------------------------------------------------
            "append file": self.append,
            "af": self.append,

            # --------------------------------------------------
            # Create Folder
            # --------------------------------------------------
            "create folder": self.mkdir,
            "mkdir": self.mkdir,
            "md": self.mkdir,

            # --------------------------------------------------
            # Rename File
            # --------------------------------------------------
            "rename file": self.rename,
            "ren": self.rename,

            # Copy File
            "copy file": self.copy,
            "cp": self.copy,

            # Move File
            "move file": self.move,
            "mv": self.move,

            # Delete File
            "delete file": self.delete,
            "df": self.delete,
        }

    def execute(self, text: str) -> str:
        text = text.strip()
        lower = text.lower()

        for command, handler in self.commands.items():

            # Exact command
            if lower == command:
                return handler("")

            # Command with arguments
            prefix = command + " "

            if lower.startswith(prefix):
                argument = text[len(prefix):].strip()
                return handler(argument)

        return self.help()

    # --------------------------------------------------
    # Controllers
    # --------------------------------------------------

    def current_directory(self, _: str) -> str:
        return current_directory()

    def list_directory(self, _: str) -> str:
        return list_directory()

    def read(self, argument: str) -> str:
        if not argument:
            return (
                "Usage:\n"
                "read file <filename>\n"
                "rf <filename>"
            )

        return read_file(argument)

    def create(self, argument: str) -> str:
        if not argument:
            return (
                "Usage:\n"
                "create file <filename>\n"
                "cf <filename>"
            )

        return create_file(argument)

    def write(self, argument: str) -> str:
        parts = argument.split(maxsplit=1)

        if len(parts) < 2:
            return (
                "Usage:\n"
                "write file <filename> <text>\n"
                "wf <filename> <text>"
            )

        filename = parts[0]
        content = parts[1]

        return write_file(
            filename,
            content,
        )

    def append(self, argument: str) -> str:
        parts = argument.split(maxsplit=1)

        if len(parts) < 2:
            return (
                "Usage:\n"
                "append file <filename> <text>\n"
                "af <filename> <text>"
            )

        filename = parts[0]
        content = parts[1]

        return append_file(
            filename,
            content,
        )

    def mkdir(self, argument: str) -> str:
        if not argument:
            return (
                "Usage:\n"
                "create folder <foldername>\n"
                "mkdir <foldername>\n"
                "md <foldername>"
            )

        return create_folder(argument)
    
    def rename(self, argument: str) -> str:
        parts = argument.split(maxsplit=1)

        if len(parts) < 2:
            return (
                "Usage:\n"
                "rename file <old> <new>\n"
                "ren <old> <new>"
            )

        old_name = parts[0]
        new_name = parts[1]

        return rename_file(
            old_name,
            new_name
        )
    
    def copy(self, argument: str) -> str:
        parts = argument.split(maxsplit=1)

        if len(parts) < 2:
            return (
                "Usage:\n"
                "copy file <source> <destination>\n"
                "cp <source> <destination>"
            )

        return copy_file(parts[0], parts[1])
    
    def move(self, argument: str) -> str:
        parts = argument.split(maxsplit=1)

        if len(parts) < 2:
            return (
                "Usage:\n"
                "move file <source> <destination>\n"
                "mv <source> <destination>"
            )

        return move_file(parts[0], parts[1])

    def delete(self, argument: str) -> str:
        if not argument:
            return (
                "Usage:\n"
                "delete file <filename>\n"
                "df <filename>"
            )

        return delete_file(argument)

    # --------------------------------------------------
    # Help
    # --------------------------------------------------

    def help(self) -> str:
        return (
            "Supported Commands\n\n"

            "[Directory]\n"
            "- current directory\n"
            "- pwd\n"
            "- where am i\n"
            "- list files\n"
            "- show files\n"
            "- dir\n"
            "- ls\n\n"

            "[Read File]\n"
            "- read file <filename>\n"
            "- rf <filename>\n\n"

            "[Create File]\n"
            "- create file <filename>\n"
            "- cf <filename>\n\n"

            "[Write File]\n"
            "- write file <filename> <text>\n"
            "- wf <filename> <text>\n\n"

            "[Append File]\n"
            "- append file <filename> <text>\n"
            "- af <filename> <text>"

            "\n[Create Folder]\n"
            "- create folder <foldername>\n"
            "- mkdir <foldername>\n"
            "- md <foldername>" 

              "\n[Rename File]\n"
            "- rename file <old> <new>\n"
            "- ren <old> <new>"

            "\n[Copy File]\n"
            "- copy file <source> <destination>\n"
            "- cp <source> <destination>"

            "\n[Move File]\n"
            "- move file <source> <destination>\n"
            "- mv <source> <destination>"

            "\n[Delete File]\n"
            "- delete file <filename>\n"
            "- df <filename>"
        )