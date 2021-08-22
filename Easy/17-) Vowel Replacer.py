"""
Create a function that replaces all the vowels in a string with a specified character.

Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
"""


def replace_vowels(txt, ch):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for letter in txt:
        if letter in vowels:
            new_string += ch

        else:
            new_string += letter
    return new_string


print(replace_vowels("shakespeare", "*"))
