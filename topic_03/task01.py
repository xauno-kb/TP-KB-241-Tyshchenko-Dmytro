while True:
    command = input("Enter 'exit' to quit or press Enter to continue: ")
    if command.lower() == 'exit':
        break
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        if op == '+':
            print("Result:", num1 + num2)
        elif op == '-':
            print("Result:", num1 - num2)
        elif op == '*':
            print("Result:", num1 * num2)
        elif op == '/':
            print("Result:", num1 / num2)
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
