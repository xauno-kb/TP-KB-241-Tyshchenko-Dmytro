from calculator import Calculator
from input_handler import InputHandler

def main():
    calculator = Calculator()

    operation = InputHandler.get_operation()
    a, b = InputHandler.get_numbers()

    if operation == "+":
        result = calculator.add(a, b)
    elif operation == "-":
        result = calculator.sub(a, b)
    elif operation == "*":
        result = calculator.mul(a, b)
    elif operation == "/":
        result = calculator.div(a, b)
    else:
        result = "Невідома операція"

    print("Результат:", result)


if __name__ == "__main__":
    main()
