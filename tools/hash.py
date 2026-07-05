import hashlib

from tools.core.base import BaseTool


class HashTool(BaseTool):
    name = "Hash Generator"
    description = "Generate hashes using common algorithms."
    version = "1.0"
    author = "Rajveerr"
    enabled = True

    keywords = (
        "hash",
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
    )

    def execute(self, text: str) -> str:
        text = text.strip()

        parts = text.split(maxsplit=1)

        if len(parts) < 2:
            return (
                "Usage:\n"
                "hash <text>\n"
                "md5 <text>\n"
                "sha256 <text>"
            )

        algorithm = parts[0].lower()
        data = parts[1].encode()

        if algorithm == "hash":
            algorithm = "sha256"

        algorithms = {
            "md5": hashlib.md5,
            "sha1": hashlib.sha1,
            "sha224": hashlib.sha224,
            "sha256": hashlib.sha256,
            "sha384": hashlib.sha384,
            "sha512": hashlib.sha512,
        }

        if algorithm not in algorithms:
            return (
                f"Unsupported algorithm: {algorithm}"
            )

        digest = algorithms[algorithm](data).hexdigest()

        return (
            f"{algorithm.upper()} Hash\n\n"
            f"{digest}"
        )