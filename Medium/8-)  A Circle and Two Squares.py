"""
Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a
circumcircle and for the bigger one, an incircle.


Create a function, that takes an integer (radius of the circle) and returns the difference
of the areas of the two squares.

Examples
square_areas_difference(5) ➞ 50

square_areas_difference(6) ➞ 72

square_areas_difference(7) ➞ 98
"""
from math import sqrt


def square_areas_difference(r):
    return round((2 * r * 2 * r) - (sqrt(r ** 2 + r ** 2) * sqrt(r ** 2 + r ** 2)))


print(square_areas_difference(6))
