"""
Create a function that takes a string, checks if it has the
same number of "x"s and "o"s and returns either True or False.

Return a boolean value (True or False).
Return True if the amount of x's and o's are the same.
Return False if they aren't the same amount.
The string can contain any character.
When "x" and "o" are not in the string, return True.
Examples
XO("ooxx") ➞ True

XO("xooxx") ➞ False

XO("ooxXm") ➞ True
# Case insensitive.

XO("zpzpzpp") ➞ True
# Returns True if no x and o.

XO("zzoo") ➞ False
"""


def XO(txt):
    x_count = 0
    o_count = 0
    for letter in txt:
        if letter.lower() == "x":
            x_count += 1
        elif letter.lower() == "o":
            o_count += 1
    if x_count == o_count:
        return True
    elif x_count != o_count:
        return False


print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))
