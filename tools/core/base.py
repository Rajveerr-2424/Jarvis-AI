from abc import ABC, abstractmethod


class BaseTool(ABC):

    name = "Unnamed"

    description = ""

    version = "1.0"

    author = "Rajveerr"

    enabled = True

    calls = 0

    errors = 0

    last_used = None

    average_time = 0

    @abstractmethod
    def can_handle(self, text: str) -> bool:
        """Return True if this tool should handle the request."""
        pass

    @abstractmethod
    def execute(self, text: str):
        """Execute the tool."""
        pass