from tools.core.base import BaseTool


class CalculatorTool(BaseTool):
    name = "Calculator"
    description = "Evaluate arithmetic expressions."
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    def can_handle(self, text: str) -> bool:
        allowed = "0123456789+-*/(). %"

        text = text.strip()

        return (
            len(text) > 0
            and all(char in allowed for char in text)
        )

    def execute(self, text: str) -> str | None:
        try:
            result = eval(text)
            return str(result)
        
        except ZeroDivisionError:
            return "Sorry Sir, division by zero is undefined."

        except Exception:
            return None