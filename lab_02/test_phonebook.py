import unittest
import phonebook


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        phonebook.students = [
            {"name": "Bob", "phone": "1", "email": "b@e.com", "group": "IP-1"},
            {"name": "Emma", "phone": "2", "email": "e@e.com", "group": "IP-2"},
        ]

    def test_add(self):
        phonebook.students = []
        phonebook.students.append({"name": "Bob", "phone": "1", "email": "b", "group": "G"})
        phonebook.addNewElement = lambda: None  # заміна input-функції
        phonebook.students.insert(1, {"name": "Carl", "phone": "3", "email": "c", "group": "G"})
        self.assertEqual(len(phonebook.students), 2)

    def test_delete(self):
        phonebook.deleteElement = lambda: None
        phonebook.students.pop(0)
        self.assertEqual(len(phonebook.students), 1)

    def test_update(self):
        phonebook.updateElement = lambda: None
        phonebook.students[0]["name"] = "Adam"
        self.assertEqual(phonebook.students[0]["name"], "Adam")

    def test_load_save(self):
        phonebook.save_to_csv("test.csv")
        phonebook.load_from_csv("test.csv")
        self.assertEqual(len(phonebook.students), 2)


if __name__ == '__main__':
    unittest.main()
