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

    match op:
        case "+":
            print("Результат:", add(a, b))
        case "-":
            print("Результат:", subtract(a, b))
        case "*":
            print("Результат:", multiply(a, b))
        case "/":
            print("Результат:", divide(a, b))
        case _:
            print("Невідома операція!")
