"""
Create a function that takes voltage and current and returns the calculated power.

Examples
circuit_power(230, 10) ➞ 2300

circuit_power(110, 3) ➞ 330

circuit_power(480, 20) ➞ 9600
"""


def circuit_power(voltage, current):
    return voltage * current


print(circuit_power(110, 3))
