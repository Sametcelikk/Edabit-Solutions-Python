"""
"Loves me, loves me not" is a traditional game in which a person plucks off
all the petals of a flower one by one, saying the phrase "Loves me" and
"Loves me not" when determining whether the one that they love, loves them back.

Given a number of petals, return a string which repeats the phrases
"Loves me" and "Loves me not" for every alternating petal, and return
the last phrase in all caps. Remember to put a comma and space between phrases.

Examples
loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"

loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"

loves_me(1) ➞ "LOVES ME"

Notes
Remember to return a string.
The first phrase is always "Loves me".
"""


def loves_me(n):
    resultString = ""
    for i in range(1, n + 1):
        if i == n and i % 2 == 0:
            resultString += "LOVES ME NOT"
            return resultString
        elif i == n and i % 2 != 0:
            resultString += "LOVES ME"
            return resultString
        elif i % 2 != 0:
            resultString += "Loves me, "
        elif i % 2 == 0:
            resultString += "Loves me not, "


print(loves_me(33))
