import csv
import os

students = []


def load_from_csv(filename):
    global students
    students = []

    if not os.path.exists(filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "phone", "email", "group"])
            writer.writerow(["Bob", "0631234567", "bob@example.com", "IP-21"])
            writer.writerow(["Emma", "0631234567", "emma@example.com", "IP-22"])
            writer.writerow(["Jon", "0631234567", "jon@example.com", "IP-21"])
            writer.writerow(["Zak", "0631234567", "zak@example.com", "IP-23"])

    with open(filename, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            students.append({
                "name": row["name"],
                "phone": row["phone"],
                "email": row["email"],
                "group": row["group"]
            })

    students.sort(key=lambda x: x["name"])


def save_to_csv(filename):
    with open(filename, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["name", "phone", "email", "group"])
        writer.writeheader()
        writer.writerows(students)


def printAllList():
    for elem in students:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, "
              f"Email: {elem['email']}, Group: {elem['group']}")


def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    students.insert(insertPosition, newItem)
    print("New element has been added")


def deleteElement():
    name = input("Please enter name to be deleted: ")

    deletePosition = -1
    for item in students:
        if item["name"] == name:
            deletePosition = students.index(item)
            break

    if deletePosition == -1:
        print("Element was not found")
    else:
        del students[deletePosition]
        print(f"Student '{name}' has been deleted")


def updateElement():
    name = input("Please enter name to be updated: ")

    updateIndex = -1
    for item in students:
        if item["name"] == name:
            updateIndex = students.index(item)
            break

    if updateIndex == -1:
        print("Element was not found")
        return

    print("Leave field empty if you don't want to change it.")
    new_name = input(f"New name [{students[updateIndex]['name']}]: ") or students[updateIndex]['name']
    new_phone = input(f"New phone [{students[updateIndex]['phone']}]: ") or students[updateIndex]['phone']
    new_email = input(f"New email [{students[updateIndex]['email']}]: ") or students[updateIndex]['email']
    new_group = input(f"New group [{students[updateIndex]['group']}]: ") or students[updateIndex]['group']

    del students[updateIndex]

    updatedItem = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "group": new_group
    }

    insertPosition = 0
    for item in students:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break

    students.insert(insertPosition, updatedItem)
    print("Element has been updated")


def main():
    filename = "students.csv"
    load_from_csv(filename)

    while True:
        choice = input("Choose action [C create, U update, D delete, P print, X exit]: ")
        match choice.lower():
            case "c":
                addNewElement()
            case "u":
                updateElement()
            case "d":
                deleteElement()
            case "p":
                printAllList()
            case "x":
                print("Saving CSV...")
                save_to_csv(filename)
                print("Exit.")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()