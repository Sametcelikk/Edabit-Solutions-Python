"""
Create a function that returns True if a given inequality expression is correct and False otherwise.

Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
"""


def correct_signs(txt):
    answer = eval(txt)
    return answer


print(correct_signs("1 < 2 < 6 < 9 > 3"))
print(correct_signs("13 > 44 > 33 > 1"))
