# write a program to figure out whether given number  is perfect number or not

number = int(input("Enter number : ")) 
sum = 0
divisor = 1
while divisor<number: 
    reminder = number % divisor
    if reminder == 0:
        sum = sum + divisor
    divisor = divisor + 1 

if sum == number:
    print("it is perfect number")
else:
    print("it is not perfect number")