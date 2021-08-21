"""
Create a function that checks to see if two object arguments are equal to one another.
Return True if the objects are equal, otherwise, return False.

Examples
# The first object parameter.

obj_one = {
  "name": "Benny",
  "phone": "3325558745",
  "email": "benny@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}


is_equal(obj_one, obj_two)
➞ False
# The first object parameter.

obj_one = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}

# The second object parameter.

obj_two = {
  "name": "Jason",
  "phone": "9853759720",
  "email": "jason@edabit.com"
}


is_equal(obj_one, obj_two)
➞ True
"""

coustumerDict1 = {
    "name": "Benny",
    "phone": "3325558745",
    "email": "benny@edabit.com"
}
coustumerDict2 = {
    "name": "Jason",
    "phone": "9853759720",
    "email": "jason@edabit.com"
}


def is_equal(obj_one, obj_two):
    if obj_one == obj_two:
        return True
    elif obj_one != obj_two:
        return False


print(is_equal(coustumerDict1, coustumerDict1))  # Same objects
print(is_equal(coustumerDict1, coustumerDict2))  # Different objects
