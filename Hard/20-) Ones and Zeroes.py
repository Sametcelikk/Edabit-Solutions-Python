"""
Write a function that returns True if every consecutive sequence of ones is
followed by a consecutive sequence of zeroes of the same length.

Examples
same_length("110011100010") ➞ True

same_length("101010110") ➞ False

same_length("111100001100") ➞ True

same_length("111") ➞ False"""


def same_length(txt):
    counter1 = 0
    counter0 = 0
    for i in txt:
        if i == "1":
            counter1 += 1
        elif i == "0":
            counter0 += 1
    if counter1 == counter0:
        return True
    elif counter1 != counter0:
        return False


print(same_length("110011100010"))
print(same_length("111100001100"))
print(same_length("111"))
