#write a program to count digits in given string 

line = input("Enter a string: ")
digit_count = 0
for char in line:
    if char.isdigit():
        digit_count += 1
print("Number of digits:", digit_count)