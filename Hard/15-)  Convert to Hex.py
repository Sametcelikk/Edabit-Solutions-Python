"""
Create a function that takes a strings characters as ASCII and returns each
characters hexadecimal value as a string.

Examples
convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"

convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"

convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"

Notes
Each byte must be seperated by a space.
All alpha hex characters must be lowercase.
"""


def convert_to_hex(txt):
    newTxt = ""
    for i in txt:
        unicodeCharacter = ord(i)
        newTxt += hex(unicodeCharacter)[2::] + " "
    return newTxt[0:-1:]


print(convert_to_hex("hello world"))
print(convert_to_hex("Big Boi"))

"""a=ord("0")
print(a)
print(hex(a)[2::])"""
