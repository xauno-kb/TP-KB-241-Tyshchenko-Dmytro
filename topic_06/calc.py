from functions import add, sub, mul, div
from operations import get_numbers, get_operation
from logger import logger

op = get_operation()
a, b = get_numbers()

if op == "+":
    result = add(a, b)
elif op == "-":
    result = sub(a, b)
elif op == "*":
    result = mul(a, b)
elif op == "/":
    result = div(a, b)
else:
    logger.warning(f"Невідома операція: {op}")
    result = "Невідома операція"

print(result)
