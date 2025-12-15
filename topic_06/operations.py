from logger import logger

def get_numbers():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    logger.info(f"Введені числа: a={a}, b={b}")
    return a, b

def get_operation():
    op = input("Оберіть операцію (+, -, *, /): ")
    logger.info(f"Обрана операція: {op}")
    return op
