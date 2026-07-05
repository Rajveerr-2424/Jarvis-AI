from datetime import datetime

from tools.core.base import BaseTool


class TimeTool(BaseTool):
    name = "Time"
    description = "Returns the current date and time."
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    keywords = (
        "time",
        "date",
        "today",
        "day",
        "clock",
    )

    def execute(self, text: str) -> str:
        now = datetime.now()

        current_date = now.strftime("%d %B %Y")
        current_day = now.strftime("%A")
        current_time = now.strftime("%I:%M:%S %p")

        return (
            f"Current Date : {current_date}\n"
            f"Current Day  : {current_day}\n"
            f"Current Time : {current_time}"
        )