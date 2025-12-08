from __future__ import annotations
import json
from pathlib import Path
from typing import List, Dict, Any


class FileManager:
    """Клас для зчитування/запису JSON-даних про студентів."""


    @staticmethod
    def read_json(path: str) -> List[Dict[str, Any]]:
        p = Path(path)
        if not p.exists():
            return []
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)


    @staticmethod
    def write_json(path: str, data: List[Dict[str, Any]]) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)