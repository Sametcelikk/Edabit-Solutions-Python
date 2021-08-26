"""
Write a function that transforms a list of characters into a list of dictionaries, where:

The keys are the characters themselves.
The values are the ASCII codes of those characters.
Examples
to_dict(["a", "b", "c"]) ➞ [{"a": 97}, {"b": 98}, {"c": 99}]

to_dict(["^"]) ➞ [{"^": 94}]

to_dict([]) ➞ []
"""


def to_dict(lst):
    list1 = []
    for i in lst:
        list1.append({i: ord(i)})

    return list1


print(to_dict(["a", "b", "c"]))

"""
      OTHER SOLUTION
      
def to_dict(lst):
    return [{c: ord(c)} for c in lst]


print(to_dict(["a", "b", "c"]))"""
