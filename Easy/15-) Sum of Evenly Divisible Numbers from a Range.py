"""
Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
"""


def evenly_divisible(a, b, c):
    list1 = list(range(a, b + 1))
    list2 = []
    for index in list1:
        if index % c == 0:
            list2.append(index)
    return sum(list2)


print(evenly_divisible(1, 10, 20))
print(evenly_divisible(1, 10, 2))
