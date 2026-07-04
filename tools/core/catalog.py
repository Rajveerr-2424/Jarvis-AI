from tools.calculator import CalculatorTool


class ToolCatalog:
    """
    Stores information about every available tool.
    """

    def __init__(self):
        self.tools = {
            CalculatorTool.name: CalculatorTool()
        }

    def all(self):
        return list(self.tools.values())

    def get(self, name: str):
        return self.tools.get(name)