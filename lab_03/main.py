from datetime import datetime
from Student import Student
from StudentList import StudentList


DATA_FILE = "data/students.json"


MENU = """
Меню:
1) Показати всіх студентів
2) Додати студента
3) Видалити студента за id
4) Оновити дані студента
5) Завантажити з файлу
6) Зберегти в файл
0) Вихід
"""




def parse_date(s: str):
    return datetime.fromisoformat(s).date()




def main():
    sl = StudentList()
    try:
        sl.load_from_file(DATA_FILE)
        print(f"Завантажено {len(sl.list_all())} студентів з {DATA_FILE}")
    except Exception:
        print("Не вдалося завантажити дані — використовуємо порожній список")


    while True:
        print(MENU)
        choice = input("Оберіть дію: ").strip()
        if choice == "1":
            for s in sl.list_all():
                print(s)
        elif choice == "2":
            sid = int(input("id: "))
            fn = input("Ім'я: ")
            ln = input("Прізвище: ")
            bd = parse_date(input("Дата народження (YYYY-MM-DD): "))
            grades_raw = input("Оцінки через кому (порожньо якщо немає): ")
            grades = [float(x.strip()) for x in grades_raw.split(",") if x.strip()] if grades_raw.strip() else []
            st = Student(student_id=sid, first_name=fn, last_name=ln, birthdate=bd, grades=grades)
            try:
                sl.add_student(st)
                print("Додано")
            except ValueError as e:
                print(e)
        elif choice == "3":
            sid = int(input("id студента для видалення: "))
            ok = sl.remove_student_by_id(sid)
            print("Видалено" if ok else "Студента не знайдено")
        elif choice == "4":
            sid = int(input("id студента для оновлення: "))
            s = sl.find_by_id(sid)
            if not s:
                print("Не знайдено")
                continue
            print("Залиште поле порожнім щоб не змінювати")
            fn = input(f"Ім'я [{s.first_name}]: ") or s.first_name
            ln = input(f"Прізвище [{s.last_name}]: ") or s.last_name
            bd_in = input(f"Дата народження [{s.birthdate.isoformat()}]: ")
            bd = s.birthdate if not bd_in.strip() else parse_date(bd_in)
            grades_in = input(f"Оцінки через кому [{', '.join(map(str,s.grades))}]: ")
            grades = s.grades if not grades_in.strip() else [float(x.strip()) for x in grades_in.split(",") if x.strip()]
            sl.update_student(sid, first_name=fn, last_name=ln, birthdate=bd, grades=grades)
            print("Оновлено")
        elif choice == "5":
            path = input(f"Шлях до файлу (за замовчуванням {DATA_FILE}): ") or DATA_FILE
            sl.load_from_file(path)
            print("Завантажено")
        elif choice == "6":
            path = input(f"Шлях до файлу (за замовчуванням {DATA_FILE}): ") or DATA_FILE
            sl.save_to_file(path)
            print("Збережено")
        elif choice == "0":
            print("До побачення")
            break
        else:
            print("Невірна команда")




if __name__ == '__main__':
    main()