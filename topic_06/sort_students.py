students = [
    {"name": "Іван", "grade": 85},
    {"name": "Олена", "grade": 92},
    {"name": "Петро", "grade": 78},
    {"name": "Марія", "grade": 92},
]

print("Початковий список:")
for student in students:
    print(student)

sorted_by_name = sorted(
    students,
    key=lambda student: student["name"]
)

print("\nВідсортовано за ім'ям:")
for student in sorted_by_name:
    print(student)

sorted_by_grade = sorted(
    students,
    key=lambda student: student["grade"]
)

print("\nВідсортовано за оцінкою:")
for student in sorted_by_grade:
    print(student)
