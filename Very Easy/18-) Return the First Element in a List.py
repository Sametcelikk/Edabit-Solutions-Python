"""
Create a function that takes a list containing only numbers and return the first element.

Examples
get_first_value([1, 2, 3]) ➞ 1

get_first_value([80, 5, 100]) ➞ 80

get_first_value([-500, 0, 50]) ➞ -500
"""

numbersList = [5, 3, 7, 1]


def get_first_value(number_list):
    return number_list[0]


print(get_first_value(numbersList))