"""
Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

Examples
format_date("11/12/2019") ➞ "20191211"

format_date("12/31/2019") ➞ "20193112"

format_date("01/15/2019") ➞ "20191501"
"""


def format_date(date):
    string = date
    return string[6::] + string[3:5:] + string[0:2:]


print(format_date("11/12/2019"))
