#Excersise: Convert Minutes into Hours and Minutes
min = int(input("Enter Minutes : "))

hour = min//60
min = min%60

print(hour," Hours ",min,"Minutes")