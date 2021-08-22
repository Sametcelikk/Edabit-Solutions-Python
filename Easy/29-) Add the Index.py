"""
Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...

Examples
add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]

add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]

add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
"""


def add_indexes(lst):
    index = 0
    answerList = []
    for i in lst:
        answerList.append(i + index)
        index += 1
    return answerList


print(add_indexes([1, 2, 3, 4, 5]))
