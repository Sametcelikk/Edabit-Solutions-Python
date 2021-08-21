"""
Create a function that takes a base number and an exponent number and returns the calculation.

Examples
calculate_exponent(5, 5) ➞ 3125

calculate_exponent(10, 10) ➞ 10000000000

calculate_exponent(3, 3) ➞ 27
"""


def calculate_exponent(num, exp):
    return pow(num, exp)


print(calculate_exponent(5, 5))

"""
pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.
"""
