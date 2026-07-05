# Handles all file-related tool operations.

from tools.core.base import BaseTool

from tools.filesystem.append import append_file
from tools.filesystem.create import create_file
from tools.filesystem.current import current_directory
from tools.filesystem.listdir import list_directory
from tools.filesystem.read import read_file
from tools.filesystem.write import write_file


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
        )