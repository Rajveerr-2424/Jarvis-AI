from tools.core.catalog import ToolCatalog


class ToolManager:
    def __init__(self):
        self.catalog = ToolCatalog()

    def process(self, text):
        for tool in self.catalog.all():

            if not tool.enabled:
                continue

            if tool.can_handle(text):
                response = tool.execute(text)
                return tool, response

        return None, None

    def list_tools(self):
        return self.catalog.all()