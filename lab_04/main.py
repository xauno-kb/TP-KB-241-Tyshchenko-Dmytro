import re
import math

def to_rpn(expression: str):
    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    right_assoc = {'^'}

    output = []
    stack = []

    tokens = re.findall(r"\d+\.?\d*|[()+\-*/^]", expression.replace(" ", ""))

    for token in tokens:
        if re.fullmatch(r"\d+\.?\d*", token):
            output.append(token)
        elif token in priority:
            while stack and stack[-1] != '(' and \
                  ((priority[stack[-1]] > priority[token]) or
                   (priority[stack[-1]] == priority[token] and token not in right_assoc)):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return output

def eval_rpn(rpn_tokens):
    stack = []

    for token in rpn_tokens:
        if re.fullmatch(r"\d+\.?\d*", token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            match token:
                case '+': stack.append(a + b)
                case '-': stack.append(a - b)
                case '*': stack.append(a * b)
                case '/': stack.append(a / b)
                case '^': stack.append(a ** b)

    return stack[0]

def main():
    expr = input("Введіть математичний вираз: ")

    rpn = to_rpn(expr)
    print("ЗПН:", " ".join(rpn))

    result = eval_rpn(rpn)
    print("Результат:", result)


if __name__ == "__main__":
    main()
