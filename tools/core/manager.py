from tools.core.catalog import ToolCatalog


class ToolManager:
    def __init__(self):
        self.catalog = ToolCatalog()

    def process(self, text: str):
        """
        Try every enabled tool until one claims the request.
        """

        for tool in self.catalog.all():

            if not tool.enabled:
                continue

            handled = tool.can_handle(text)

            # Uncomment while debugging routing issues.
            # print(f"[ToolManager] {tool.name}: {handled}")

            if handled:
                response = tool.execute(text)
                return tool, response

        return None, None

    def list_tools(self):
        return self.catalog.all()

    # def debug(self, text: str):
    #     """
    #     Shows which tools match a given command.
    #     Useful for debugging routing problems.
    #     """

    #     print(f"\nInput: {text}\n")

    #     for tool in self.catalog.all():
    #         print(
    #             f"{tool.name:<15} "
    #             f"{'Enabled' if tool.enabled else 'Disabled':<10} "
    #             f"Match = {tool.can_handle(text)}"
    #         )