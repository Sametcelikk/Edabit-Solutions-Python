"""
A city skyline can be represented as a 2-D list with 1s representing buildings.
In the example below, the height of the tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
Create a function that takes a skyline (2-D list of 0's and 1's) and
returns the height of the tallest skyscraper.

Examples
tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 3

tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 4

tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 2
"""


def tallest_skyscraper(lst):
    block1 = 0
    block2 = 0
    block3 = 0
    block4 = 0
    lst2 = []
    for i in lst:
        block1 += i[0]
        block2 += i[1]
        block3 += i[2]
        block4 += i[3]
    lst2.append(block1)
    lst2.append(block2)
    lst2.append(block3)
    lst2.append(block4)
    lst2.sort()
    return lst2[-1]


print(tallest_skyscraper(
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]
))

print(tallest_skyscraper(
    [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1]
    ]
))
