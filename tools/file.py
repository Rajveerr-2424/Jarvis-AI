from tools.core.base import BaseTool

from tools.filesystem.current import current_directory
from tools.filesystem.listdir import list_directory
from tools.filesystem.read import read_file
from tools.filesystem.create import create_file


class FileTool(BaseTool):
    name = "File"
    description = "File system operations."
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    keywords = (
        "current directory",
        "pwd",
        "where am i",
        "list files",
        "show files",
        "dir",
        "ls",
        "read file",
        "open",
        "cat",
        "create file",
        "touch",
    )

    def __init__(self):
        self.commands = {
            # Current directory
            "current directory": lambda _: current_directory(),
            "pwd": lambda _: current_directory(),
            "where am i": lambda _: current_directory(),

            # Directory listing
            "list files": lambda _: list_directory(),
            "show files": lambda _: list_directory(),
            "dir": lambda _: list_directory(),
            "ls": lambda _: list_directory(),

            # Read file
            "read file": read_file,
            "open": read_file,
            "cat": read_file,

            # Create file
            "create file": create_file,
            "touch": create_file,
        }

    def execute(self, text: str) -> str:
        text = text.strip()

        for command, handler in self.commands.items():

            # Exact commands
            if text.lower() == command:
                return handler("")

            # Commands with arguments
            prefix = command + " "

            if text.lower().startswith(prefix):
                argument = text[len(prefix):].strip()
                return handler(argument)

        return self.help()

    def help(self):
        return (
            "Supported Commands\n\n"
            "- current directory\n"
            "- pwd\n"
            "- where am i\n"
            "- list files\n"
            "- show files\n"
            "- dir\n"
            "- ls\n"
            "- read file <filename>\n"
            "- open <filename>\n"
            "- cat <filename>\n"
            "- create file <filename>\n"
            "- touch <filename>"
        )