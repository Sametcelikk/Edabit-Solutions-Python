"""
Create a function to test if a string is a valid pin or not.

A valid pin has:

Exactly 4 or 6 characters.
Only numerical characters (0-9).
No whitespace.
Examples
valid("1234") ➞ True

valid("45135") ➞ False

valid("89abc1") ➞ False

valid("900876") ➞ True

valid(" 4983") ➞ False

Notes
Empty strings should return False when tested.
"""


def valid(txt):
    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    for i in txt:
        if i not in numbers:
            return False
        elif len(txt) != 6 and len(txt) != 4:
            return False

    return True


print(valid("1234"))
print(valid("45135"))
print(valid(" 4983"))
