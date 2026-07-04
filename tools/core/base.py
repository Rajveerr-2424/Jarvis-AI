from abc import ABC, abstractmethod


class BaseTool(ABC):
    name: str
    description: str

    @abstractmethod
    def can_handle(self, text: str) -> bool:
        """Return True if this tool should handle the request."""
        pass

    @abstractmethod
    def execute(self, text: str):
        """Execute the tool."""
        pass