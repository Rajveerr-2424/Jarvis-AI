from pathlib import Path
import sqlite3

DATABASE_DIR = Path("database")
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATABASE_DIR / "jarvis.db"


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.connection.row_factory = sqlite3.Row

    def cursor(self):
        return self.connection.cursor()

    def execute(self, query: str, params: tuple = ()):
        cursor = self.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor

    def close(self):
        self.connection.close()