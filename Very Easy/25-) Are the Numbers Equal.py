"""
Create a function that returns True when num1 is equal to num2; otherwise return False.

Examples
is_same_num(4, 8) ➞ False

is_same_num(2, 2) ➞  True

is_same_num(2, "2") ➞ False
"""


def is_same_num(num1, num2):
    if num1 == num2:
        return True
    elif num1 != num2:
        return False


print(is_same_num(4, 8))
print(is_same_num(2, 2))
