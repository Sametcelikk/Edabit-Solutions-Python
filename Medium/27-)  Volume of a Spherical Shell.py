"""
The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed
volume of the inner sphere:


Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to
the nearest thousandth.


Examples
vol_shell(3, 3) ➞ 0

vol_shell(7, 2) ➞ 1403.245

vol_shell(3, 800) ➞ 2144660471.753
"""
from math import pi

def vol_shell(r1, r2):
    if r1 > r2:
        return round(4/3*pi*(r1**3-r2**3),3)
    elif r2 > r1:
        return round(4/3*pi*(r2**3-r1**3),3)
    else:
        return round(4/3*pi*(r2**3-r1**3),3)

print(vol_shell(7, 2))
print(vol_shell(3, 3))