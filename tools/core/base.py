from abc import ABC, abstractmethod


class BaseTool(ABC):
    """
    Base class for every JARVIS tool.
    """

    name = "Unnamed Tool"
    description = ""
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    keywords = ()

    def can_handle(self, text: str) -> bool:
        """
        Default keyword matching.
        """
        text = text.lower()

        return any(
            keyword in text
            for keyword in self.keywords
        )

    @abstractmethod
    def execute(self, text: str):
        pass