"""
Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.

Examples
convert(1, 3) ➞ 3780

convert(2, 0) ➞ 7200

convert(0, 0) ➞ 0
"""


def convert(hours, minutes):
    return (hours * 3600) + (minutes * 60)


print(convert(1, 3))
