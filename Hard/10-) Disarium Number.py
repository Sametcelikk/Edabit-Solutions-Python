"""
A number is said to be Disarium if the sum of its digits raised to their
respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

Examples
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True
"""


def is_disarium(n):
    base = 1
    result = 0
    for i in str(n):
        result += int(i) ** base
        base += 1
    if result == n:
        return True
    else:
        return False


print(is_disarium(75))
print(is_disarium(135))
