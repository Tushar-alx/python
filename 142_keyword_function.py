#demonstrate example of keyword function

def greet(name, age):
    print("Hello", name)
    print("You are", age, "years old")

# Dynamic input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calling function using keyword arguments
greet(age=age, name=name)
