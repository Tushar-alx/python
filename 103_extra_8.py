#write a program to enter a number and find sum of digits of that number

number = int(input("Enter number : ")) 
sum = 0
if number < 0:
    number = -number
while number > 0:
    rem = number % 10
    sum += rem
    number //= 10

print("Sum of digits :", sum)