from __future__ import annotations
from typing import List, Optional
from Student import Student
from Utils import FileManager


class StudentList:
    def __init__(self) -> None:
        self._students: List[Student] = []


    def add_student(self, student: Student) -> None:
        if self.find_by_id(student.student_id) is not None:
            raise ValueError(f"Student with id {student.student_id} already exists")
        self._students.append(student)


    def remove_student_by_id(self, student_id: int) -> bool:
        s = self.find_by_id(student_id)
        if s is None:
            return False
        self._students.remove(s)
        return True


    def update_student(self, student_id: int, **kwargs) -> bool:
        s = self.find_by_id(student_id)
        if s is None:
            return False
        for k, v in kwargs.items():
            if hasattr(s, k):
                setattr(s, k, v)
        return True


    def find_by_id(self, student_id: int) -> Optional[Student]:
        for s in self._students:
            if s.student_id == student_id:
                return s
        return None


    def list_all(self) -> List[Student]:
        return list(self._students)


    def load_from_file(self, path: str) -> None:
        raw = FileManager.read_json(path)
        self._students = [Student.from_dict(d) for d in raw]


    def save_to_file(self, path: str) -> None:
        raw = [s.to_dict() for s in self._students]
        FileManager.write_json(path, raw)