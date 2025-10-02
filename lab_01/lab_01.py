# already sorted list
students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "group": "IP-21"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "group": "IP-22"},
    {"name": "Jon",  "phone": "0631234567", "email": "jon@example.com",  "group": "IP-21"},
    {"name": "Zak",  "phone": "0631234567", "email": "zak@example.com",  "group": "IP-23"}
]

def printAllList():
    for elem in students:
        strForPrint = (f"Name: {elem['name']}, Phone: {elem['phone']}, "
                       f"Email: {elem['email']}, Group: {elem['group']}")
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    # find insert position
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del students[deletePosition]
        print(f"Student '{name}' has been deleted")
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updateIndex = -1
    for item in students:
        if name == item["name"]:
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

    # Remove old record
    del students[updateIndex]

    # Create updated record
    updatedItem = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "group": new_group
    }

    # Re-insert into correct position to keep list sorted
    insertPosition = 0
    for item in students:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, updatedItem)

    print("Element has been updated")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()
