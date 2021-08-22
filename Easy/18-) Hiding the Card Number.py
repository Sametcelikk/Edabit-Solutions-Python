"""
Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.

Examples
card_hide("1234123456785678") ➞ "************5678"

card_hide("8754456321113213") ➞ "************3213"

card_hide("35123413355523") ➞ "**********5523"
"""


def card_hide(card):
    return (len(card) - 4) * "*" + card[-4:]


print(card_hide("8754456321113213"))
print(card_hide("35123413355523"))
