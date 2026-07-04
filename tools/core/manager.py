class ToolManager:
    def __init__(self):
        self.tools = []

    def register(self, tool):
        self.tools.append(tool)

    def process(self, text: str):
        for tool in self.tools:
            if tool.can_handle(text):
                return tool.execute(text)

        return None