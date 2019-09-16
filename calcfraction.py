from fractions import Fraction as F
from timeit import timeit


def calculate(num1: str, num2: str, operator: str):
   # timeit()
    print("fractions calcolator")
    num1 = F(num1)
    num2 = F(num2)

    if operator == "+":
        print(num1 + num2)

    if operator == "*":
        print(num1 * num2)

    if operator == "-":
        print(num1 - num2)

    if operator == "/":
        print(num1 / num2)

    print(timeit())



