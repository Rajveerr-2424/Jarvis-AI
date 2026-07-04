import ast
import operator

from tools.core.base import BaseTool


class CalculatorTool(BaseTool):
    name = "calculator"

    description = "Evaluate arithmetic expressions."

    def can_handle(self, text: str):
        allowed = "0123456789+-*/(). "

        return (
            len(text) > 0
            and all(c in allowed for c in text)
        )

    def execute(self, text: str):
        try:
            result = eval(text)

            return str(result)

        except Exception:
            return None