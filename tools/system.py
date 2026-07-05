import platform

import psutil

from tools.core.base import BaseTool


class SystemTool(BaseTool):
    name = "System"
    description = "Displays system information."
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    keywords = (
        "system",
        "system info",
        "cpu",
        "memory",
        "ram",
        "disk",
        "battery",
        "hostname",
        "platform",
        "os",
    )

    def execute(self, text: str) -> str:
        text = text.lower()

        commands = {
            "cpu": self.cpu,
            "memory": self.memory,
            "ram": self.memory,
            "disk": self.disk,
            "battery": self.battery,
            "hostname": self.hostname,
            "os": self.os,
            "platform": self.os,
        }

        for keyword, handler in commands.items():
            if keyword in text:
                return handler()

        return self.system()

    def system(self) -> str:
        memory = psutil.virtual_memory()

        return (
            "System Information\n\n"
            f"Operating System : {platform.system()} {platform.release()}\n"
            f"Machine          : {platform.machine()}\n"
            f"Processor        : {platform.processor()}\n"
            f"Hostname         : {platform.node()}\n"
            f"Python           : {platform.python_version()}\n"
            f"CPU Usage        : {psutil.cpu_percent(interval=1)}%\n"
            f"Memory Usage     : {memory.percent}%"
        )

    def cpu(self) -> str:
        freq = psutil.cpu_freq()

        frequency = (
            f"{freq.current:.2f} MHz"
            if freq
            else "Unavailable"
        )

        return (
            "CPU Information\n\n"
            f"Usage           : {psutil.cpu_percent(interval=1)}%\n"
            f"Physical Cores  : {psutil.cpu_count(logical=False)}\n"
            f"Logical Cores   : {psutil.cpu_count(logical=True)}\n"
            f"Frequency       : {frequency}"
        )

    def memory(self) -> str:
        memory = psutil.virtual_memory()

        return (
            "Memory Information\n\n"
            f"Total      : {memory.total / (1024 ** 3):.2f} GB\n"
            f"Used       : {memory.used / (1024 ** 3):.2f} GB\n"
            f"Available  : {memory.available / (1024 ** 3):.2f} GB\n"
            f"Usage      : {memory.percent}%"
        )

    def disk(self) -> str:
        disk = psutil.disk_usage(
            psutil.disk_partitions()[0].mountpoint
        )

        return (
            "Disk Information\n\n"
            f"Total      : {disk.total / (1024 ** 3):.2f} GB\n"
            f"Used       : {disk.used / (1024 ** 3):.2f} GB\n"
            f"Free       : {disk.free / (1024 ** 3):.2f} GB\n"
            f"Usage      : {disk.percent}%"
        )

    def battery(self) -> str:
        battery = psutil.sensors_battery()

        if battery is None:
            return "Battery information is unavailable."

        if battery.secsleft in (
            psutil.POWER_TIME_UNLIMITED,
            psutil.POWER_TIME_UNKNOWN,
        ):
            remaining = "Unknown"
        else:
            hours = battery.secsleft // 3600
            minutes = (battery.secsleft % 3600) // 60
            remaining = f"{hours}h {minutes}m"

        return (
            "Battery Information\n\n"
            f"Charge      : {battery.percent}%\n"
            f"Charging    : {'Yes' if battery.power_plugged else 'No'}\n"
            f"Time Left   : {remaining}"
        )

    def hostname(self) -> str:
        return (
            "Hostname\n\n"
            f"{platform.node()}"
        )

    def os(self) -> str:
        return (
            "Operating System\n\n"
            f"System      : {platform.system()}\n"
            f"Release     : {platform.release()}\n"
            f"Version     : {platform.version()}\n"
            f"Machine     : {platform.machine()}"
        )