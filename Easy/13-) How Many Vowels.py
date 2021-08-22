"""
reate a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4
"""
vowels=["a","e","i","o","u"]

def count_vowels(txt):
    count = 0
    for index in txt.lower():
        if index in vowels:
            count+=1
    return count

print(count_vowels("Prediction"))
print(count_vowels("Celebration"))

