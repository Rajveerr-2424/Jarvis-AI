import uuid

from tools.core.base import BaseTool


class UUIDTool(BaseTool):
    name = "UUID"
    description = "Generates UUIDs."
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    keywords = (
        "uuid",
        "guid",
        "unique id",
        "unique identifier",
    )

    def execute(self, text: str) -> str:
        generated = uuid.uuid4()

        return (
            "Generated UUID\n\n"
            f"{generated}"
        )