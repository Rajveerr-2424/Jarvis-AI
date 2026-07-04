from tools.calculator import CalculatorTool


class ToolRegistry:
    """
    Central registry for all available tools.
    """

    @staticmethod
    def get_tools():
        return [
            CalculatorTool(),
        ]