import unittest
import tempfile
import os
from datetime import date
from Student import Student
from StudentList import StudentList


class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.sl = StudentList()
        self.s1 = Student(1, "Ivan", "Ivanov", date(2000,1,1), [4.0, 5.0])
        self.s2 = Student(2, "Petro", "Petrov", date(2001,2,2), [3.5])


def test_add_and_find(self):
    self.sl.add_student(self.s1)
    self.assertIsNotNone(self.sl.find_by_id(1))
    with self.assertRaises(ValueError):
        self.sl.add_student(self.s1) # duplicate id


def test_remove(self):
    self.sl.add_student(self.s1)
    self.assertTrue(self.sl.remove_student_by_id(1))
    self.assertFalse(self.sl.remove_student_by_id(1))


def test_update(self):
    self.sl.add_student(self.s2)
    ok = self.sl.update_student(2, first_name="PetroUpdated")
    self.assertTrue(ok)
    s = self.sl.find_by_id(2)
    self.assertEqual(s.first_name, "PetroUpdated")


def test_save_load_file(self):
    self.sl.add_student(self.s1)
    self.sl.add_student(self.s2)
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    try:
        self.sl.save_to_file(path)
        new_sl = StudentList()
        new_sl.load_from_file(path)
        self.assertIsNotNone(new_sl.find_by_id(1))
        self.assertIsNotNone(new_sl.find_by_id(2))
    finally:
        os.remove(path)


if __name__ == '__main__':
    unittest.main()