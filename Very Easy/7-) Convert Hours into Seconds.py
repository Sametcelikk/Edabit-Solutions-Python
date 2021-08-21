"""
Write a function that converts hours into seconds.

Examples
how_many_seconds(2) ➞ 7200

how_many_seconds(10) ➞ 36000

how_many_seconds(24) ➞ 86400
"""


def how_many_seconds(hours):
    return hours * 60 * 60


print(how_many_seconds(10))
