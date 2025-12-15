
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"


students = [
    Student("Іван", 20),
    Student("Олена", 18),
    Student("Петро", 22),
    Student("Марія", 19),
]

sorted_students = sorted(
    students,
    key=lambda student: student.age
)

print("Список студентів, відсортований за віком:")
for student in sorted_students:
    print(student)
