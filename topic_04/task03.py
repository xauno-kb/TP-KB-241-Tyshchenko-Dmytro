def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

while True:
    command = input("Enter 'exit' to quit or press Enter to continue: ")
    if command.lower() == 'exit':
        break
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        if op == '+':
            print("Result:", add(num1, num2))
        elif op == '-':
            print("Result:", subtract(num1, num2))
        elif op == '*':
            print("Result:", multiply(num1, num2))
        elif op == '/':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid number input")
