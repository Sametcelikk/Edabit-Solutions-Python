"""
You call your spouse in anger and a "little" argument takes place. Count the total amount of adjectives used.
Given a dictionary of adjectives, return the total amount of adjectives used.

Examples
total_amount_adjectives({ "a": "moron" }) ➞ 1

total_amount_adjectives({ "a": "idiot", "b": "idiot", "c": "idiot" }) ➞ 3

total_amount_adjectives({ "a": "moron", "b": "scumbag", "c": "moron", d: "dirtbag" }) ➞ 4
"""
wordsDict = {"a": "moron", "b": "scumbag", "c": "moron", "d": "dirtbag"}


def total_amount_adjectives(dct):
    valueList = []
    for key, value in dct.items():
        valueList.append(value)
    return len(valueList)


print(total_amount_adjectives(wordsDict))
