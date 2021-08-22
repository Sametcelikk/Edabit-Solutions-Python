"""
Write a function that finds the sum of the first n natural numbers. Make your function recursive.

Examples
sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15

sum_numbers(1) ➞ 1

sum_numbers(12) ➞ 78
"""


def sum_numbers(n):
    answer = 0
    for i in range(n + 1):
        answer += i
    return answer


print(sum_numbers(5))
