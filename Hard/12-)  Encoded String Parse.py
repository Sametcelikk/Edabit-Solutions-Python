"""
Create a function which takes in an encoded string and returns a dictionary according
to the following example:

Examples
parse_code("John000Doe000123") ➞ {
  "first_name": "John",
  "last_name": "Doe",
  "id": "123"
}

parse_code("michael0smith004331") ➞ {
  "first_name": "michael",
  "last_name": "smith",
  "id": "4331"
}

parse_code("Thomas00LEE0000043") ➞ {
  "first_name": "Thomas",
  "last_name": "LEE",
  "id": "43"
}
Notes

The string will always be in the same format: first name, last name and id with zeros between them.
id numbers will not contain any zeros.
"""


def parse_code(txt):
    newTxt = ""
    for i in txt:
        if i == "0":
            newTxt += " "
        else:
            newTxt += i
    lst = newTxt.split()
    dct = dict(first_name=lst[0], last_name=lst[1], id=lst[2])
    return dct


print(parse_code("michael0smith004331"))
