"""
Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

Examples
fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288

fact_of_fact(5) ➞ 34560

fact_of_fact(6) ➞ 24883200
"""

from math import factorial


def fact_of_fact(n):
    result = 1
    for number in range(0, n + 1):
        result *= factorial(number)

    return result


print(fact_of_fact(5))
