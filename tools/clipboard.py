import pyperclip

from tools.core.base import BaseTool


class ClipboardTool(BaseTool):
    name = "Clipboard"
    description = "Read, write and clear clipboard contents."
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    keywords = (
        "clipboard",
        "copy",
        "paste",
        "clear clipboard",
    )

    def execute(self, text: str) -> str:
        text = text.strip()

        lower = text.lower()

        if lower.startswith("copy "):
            return self.copy(text[5:])

        if lower == "paste":
            return self.read()

        if lower == "clipboard":
            return self.read()

        if lower == "clear clipboard":
            return self.clear()

        return (
            "Clipboard Commands\n\n"
            "• clipboard\n"
            "• paste\n"
            "• copy <text>\n"
            "• clear clipboard"
        )

    def read(self) -> str:
        content = pyperclip.paste()

        if not content:
            return "Clipboard is empty."

        return (
            "Clipboard\n\n"
            f"{content}"
        )

    def copy(self, text: str) -> str:
        pyperclip.copy(text)

        return (
            "Copied to clipboard.\n\n"
            f"{text}"
        )

    def clear(self) -> str:
        pyperclip.copy("")

        return "Clipboard cleared."