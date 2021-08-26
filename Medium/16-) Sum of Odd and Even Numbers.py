"""
Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])
"""


def sum_odd_and_even(lst):
    oddNumbers = 0
    evenNumbers = 0
    for number in lst:
        if abs(number) % 2 == 1:
            oddNumbers += number
        elif abs(number) % 2 == 0:
            evenNumbers += number
    return [evenNumbers, oddNumbers]


print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
