first_number = float(input())
second_number = float(input())
arithmetic_operation = input()


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def division(x, y):
    if y != 0:
        return x / y
    return "Division by 0!"


def multiplication(x, y):
    return x * y


def mod(x, y):
    if y == 0:
        return "Division by 0!"
    return x % y


def power(x, y):
    return x ** y


def div(x, y):
    if y == 0:
        return "Division by 0!"
    return x // y


symbols = {'+': addition, '-': subtraction, '/': division, '*': multiplication, 'mod': mod, 'pow': power, 'div': div}
print(symbols[arithmetic_operation](first_number, second_number))
