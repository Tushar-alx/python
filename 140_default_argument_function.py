# Demonstrateing example of default argument function

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

name=input("Enter your name: ")
greeting=input("Enter your greeting (or press Enter to use default): ")
if greeting:
    print(greet(name, greeting))
else:
    print(greet(name))

 