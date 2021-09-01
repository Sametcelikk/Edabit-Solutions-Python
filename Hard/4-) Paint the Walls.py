"""
Given a predetermined rate from a dictionary, write the function that will return
the time it takes for a certain amount of people to paint a certain amount of walls.
Return the minutes as an integer. No rounding is necessary.

Example
# It takes 22 minutes for 10 people to paint 10 walls.
# How many minutes does it take 14 people to paint 14 walls?

rate = {
  "people": 10,
  "walls": 10,
  "minutes": 22
}

time(rate, people, walls) ➞ 22
"""

rate = {
    "people": 10,
    "walls": 10,
    "minutes": 22
}


def time(dct, people, walls):
    return (dct['minutes'] * dct['people'] * walls) // (dct['walls'] * people)


print(time(rate, 14, 14))
