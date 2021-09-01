"""
Create a function that takes a list and string. The function should remove
the letters in the string from the list, and return the list.

Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
"""


def remove_letters(letters, word):
    for i in word:
        if i in letters:
            letters.remove(i)
    return letters


print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))
