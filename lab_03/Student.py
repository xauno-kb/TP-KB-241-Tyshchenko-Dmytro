from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List, Dict, Any


@dataclass
class Student:
    student_id: int
    first_name: str
    last_name: str
    birthdate: date
    grades: List[float] = field(default_factory=list)


    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


    def to_dict(self) -> Dict[str, Any]:
        return {
    "student_id": self.student_id,
    "first_name": self.first_name,
    "last_name": self.last_name,
    "birthdate": self.birthdate.isoformat(),
    "grades": self.grades,
    }


    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        bd = data.get("birthdate")
        if isinstance(bd, str):
            bd = datetime.fromisoformat(bd).date()
        return cls(
            student_id=int(data["student_id"]),
            first_name=str(data["first_name"]),
            last_name=str(data["last_name"]),
            birthdate=bd,
            grades=[float(g) for g in data.get("grades", [])],
        )


    def __str__(self) -> str:
        return f"{self.student_id}: {self.full_name()} (b. {self.birthdate.isoformat()})"