"""
Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation
with the given numbers.

Examples
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2
"""


def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2


print(calculator(2, "+", 2))
print(calculator(2, "*", 3))
print(calculator(4, "/", 2))
