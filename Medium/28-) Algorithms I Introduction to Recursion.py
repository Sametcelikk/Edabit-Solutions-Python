"""
Welcome to the beginning of this collection on Computer Science Algorithms.
Admittedly there are other challenges on Edabit that deal with recursion and algorithmic processes,
but these particular challenges are designed to give examples and to educate users on the topics being covered.

Recursion
In computer science, "recursion" is the act of writing a function that calls itself from within its own code.
The function below better helps explain and illustrate recursion by simply counting down from a given number to zero:

def factorial(num):
    targetNumber = 0

  if num == targetNumber:
    print("Countdown complete!")
  else:
    factorial(num - 1)

Explanation
The above function starts by initializing the target number, which is zero, then it creates a base
case by checking if the inputted number has reached the target number yet. If it has, then the function
ends and it prints the statement, else the function inputs num subtracted by one and then runs the function again.

When using recursive functions a "Base Case" is needed. A base case will stop the function once it
reaches its intended goal. In the absence of a base case, the program can either crash due to
"Stack Overflow" or by initiating an "Infinite Loop."

On a side note, initializing variables in recursive functions can sometimes be problematic because
when the function runs again it will reset the value of that variable. For this specific recursive
function the variable works fine because the target number we're trying to reach is consistently zero.

Instructions
The recursive function for this challenge should return the factorial of an inputted integer.
If anyone needs a refresher, factorials in mathematics are represented by an exclamation point
placed to the right of a number: 4! = 4 x 3 x 2 x 1 = 24

Examples
factorial(5) ➞ 120

factorial(3) ➞ 6

factorial(2) ➞ 2
"""


def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


print(factorial(5))
