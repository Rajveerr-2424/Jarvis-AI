from abc import ABC, abstractmethod
from typing import List


class BaseProvider(ABC):

    @abstractmethod
    def ask(self, messages: List[dict]) -> str:
        pass