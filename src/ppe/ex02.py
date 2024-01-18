"""Write a `convert_to_fahrenheit` function to convert the temperature in Celsius to 
the one in Fahrenheit, and a `conver_to_celsius` function to change the temperature
from Fahrenheit to Celsius.
"""

def convert_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def convert_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9