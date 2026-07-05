from tools.calculator import CalculatorTool
from tools.time import TimeTool
from tools.uuid import UUIDTool
from tools.password import PasswordTool
from tools.hash import HashTool
from tools.system import SystemTool
from tools.clipboard import ClipboardTool


class ToolCatalog:
    """
    Stores information about every available tool.
    """

    def __init__(self):
        self.tools = {
            CalculatorTool.name: CalculatorTool(),
            TimeTool.name: TimeTool(),
            UUIDTool.name: UUIDTool(),
            PasswordTool.name: PasswordTool(),
            HashTool.name: HashTool(),
            SystemTool.name: SystemTool(),
            ClipboardTool.name: ClipboardTool(),
        }

    def all(self):
        return list(self.tools.values())

    def get(self, name: str):
        return self.tools.get(name)