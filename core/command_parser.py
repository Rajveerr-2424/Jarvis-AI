from dataclasses import dataclass


@dataclass(slots=True)
class ParsedCommand:
    action: str
    resource: str
    arguments: str


class CommandParser:
    """
    Parses commands written in JCL format.

    Format:
        <action> <resource> <arguments>

    Examples:
        read file README.md
        write file notes.txt Hello
        open browser youtube.com

    NOTE:
        This parser ONLY parses.
        It does NOT validate whether the resource exists.
        Validation is performed by ToolManager.
    """

    @staticmethod
    def parse(text: str) -> ParsedCommand | None:
        text = text.strip()

        if not text:
            return None

        parts = text.split(maxsplit=2)

        if len(parts) < 2:
            return None

        action = parts[0].lower()
        resource = parts[1].lower()
        arguments = parts[2] if len(parts) == 3 else ""

        return ParsedCommand(
            action=action,
            resource=resource,
            arguments=arguments,
        )