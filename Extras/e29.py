def main():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    operator = int(input("Enter operator (1:+, 2:-, 3:*, 4:/): "))

    if operator == 1:
        print(f"Addition result: {add(first_num, second_num)}")
    elif operator == 2:
        print(f"Subtraction result: {subtract(first_num, second_num)}")
    elif operator == 3:
        print(f"Multiplication result: {multiply(first_num, second_num)}")
    elif operator == 4:
        print(f"Division result: {divide(first_num, second_num)}")

    print(type(add))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


main()
