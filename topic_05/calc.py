from functions import add, sub, mul, div
from operations import get_numbers, get_operation

op = get_operation()
a, b = get_numbers()

if op == "+":
    print(add(a, b))
elif op == "-":
    print(sub(a, b))
elif op == "*":
    print(mul(a, b))
elif op == "/":
    print(div(a, b))
else:
    print("Невідома операція")
