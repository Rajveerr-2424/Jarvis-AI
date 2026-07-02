from memory.repository import MemoryRepository

repo = MemoryRepository()
repo.initialize()

repo.remember(
    "personal",
    "name",
    "Rajveerr",
)

print(repo.recall("name"))