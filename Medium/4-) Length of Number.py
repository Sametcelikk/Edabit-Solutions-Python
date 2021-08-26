"""
Create a function that takes a number num and returns its length.

Examples
number_length(10) ➞ 2

number_length(5000) ➞ 4

number_length(0) ➞ 1
Notes
The use of the len() function is prohibited.
"""


def number_length(num):
    counter = 0
    for index in str(num):
        counter += 1
    return counter


print(number_length(10))
print(number_length(5000))
