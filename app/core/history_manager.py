import json
from pathlib import Path


class HistoryManager:

    FILE = 'history.json'

    @classmethod
    def save(cls, item):
        history = []

        if Path(cls.FILE).exists():
            with open(cls.FILE, 'r', encoding='utf-8') as f:
                history = json.load(f)

        history.append(item)

        with open(cls.FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=4)
