"""
Given a list of words in the singular form, return a set of those words
in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

Notes
This is an oversimplification of the English language so no edge cases will appear.
Only focus on whether or not to add an s to the ends of words.
"""


def pluralize(lst):
    set1 = set()
    for i in lst:
        a = lst.count(i)
        if a > 1:
            set1.add(i + "s")
        else:
            set1.add(i)

    return set1


print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))