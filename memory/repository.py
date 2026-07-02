from memory.database import Database


class MemoryRepository:
    def __init__(self):
        self.db = Database()

    def initialize(self):
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            key TEXT NOT NULL UNIQUE,
            value TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

    def remember(self, category: str, key: str, value: str):
        self.db.execute(
            """
            INSERT OR REPLACE INTO memories
            (category, key, value, updated_at)
            VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            """,
            (category, key, value),
        )

    def recall(self, key: str):
        cursor = self.db.execute(
            "SELECT value FROM memories WHERE key=?",
            (key,),
        )

        row = cursor.fetchone()

        if row:
            return row["value"]

        return None

    def forget(self, key: str):
        self.db.execute(
            "DELETE FROM memories WHERE key=?",
            (key,),
        )