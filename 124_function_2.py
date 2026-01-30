#write a program to create function that convert given fahrenheit into celsius 

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)

print(f"{fahrenheit} Fahrenheit = {celsius} Celsius.")