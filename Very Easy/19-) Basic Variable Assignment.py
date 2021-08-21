"""
A student learning Python was trying to make a function. His code should concatenate a passed string name with string "Edabit" and store it in a variable called result. He needs your help to fix this code.

Examples
name_string("Mubashir") ➞ "MubashirEdabit"

name_string("Matt") ➞ "MattEdabit"

name_string("python") ➞ "pythonEdabit"
"""


def name_string(name):
    b = "Edabit"
    result = name + b
    return result

print(name_string("Matt"))
