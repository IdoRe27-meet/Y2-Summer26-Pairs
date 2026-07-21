import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    """Load the shared memory from memory.json."""
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_memory(new_data):
    """Update the shared memory and save it."""
    memory = load_memory()

    # Update the existing memory with the new information
    memory.update(new_data)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)