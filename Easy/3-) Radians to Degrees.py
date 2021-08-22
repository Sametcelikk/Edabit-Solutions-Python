"""
Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

Examples
radians_to_degrees(1) ➞ 57.3

radians_to_degrees(20) ➞ 1145.9

radians_to_degrees(50) ➞ 2864.8
"""
from math import pi


def radians_to_degrees(rad):
    return round((rad) * (180 / pi), 1)


print(radians_to_degrees(20))
