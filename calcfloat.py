from timeit import timeit


def calculate(num1, num2, operator):

    print("float calcolator")
    num1 = float(num1)
    num2 = float(num2)

    if operator == "+":
        print(num1 + num2)

    if operator == "*":
        print(num1 * num2)

    if operator == "-":
        print(num1 - num2)

    if operator == "/":
        print(num1 / num2)

    print(timeit())

