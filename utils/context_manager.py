"""
Simple context manager that stores recent messages (in-memory).
Used to pass context to LLMs if integrated in the future.
"""

from collections import deque

class ContextManager:
    def __init__(self, max_len: int = 20):
        self.history = deque(maxlen=max_len)

    def add_message(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def get_context(self):
        return list(self.history)

    def last(self, n=5):
        return list(self.history)[-n:]
