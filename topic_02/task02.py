def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль!"

if __name__ == "__main__":
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    op = input("Введіть операцію (+, -, *, /): ")

    if op == "+":
        print("Результат:", add(a, b))
    elif op == "-":
        print("Результат:", subtract(a, b))
    elif op == "*":
        print("Результат:", multiply(a, b))
    elif op == "/":
        print("Результат:", divide(a, b))
    else:
        print("Невідома операція!")
