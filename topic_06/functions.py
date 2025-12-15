from logger import logger

def add(a, b):
    result = a + b
    logger.info(f"Операція додавання: {a} + {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    logger.info(f"Операція віднімання: {a} - {b} = {result}")
    return result

def mul(a, b):
    result = a * b
    logger.info(f"Операція множення: {a} * {b} = {result}")
    return result

def div(a, b):
    if b == 0:
        logger.error("Спроба ділення на нуль")
        return "Ділення на нуль неможливе"
    result = a / b
    logger.info(f"Операція ділення: {a} / {b} = {result}")
    return result
