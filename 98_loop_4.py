#write a program to figure out whether given number is prime number or not 
 
import sys 
number = int(input("Enter number")) 
divisor = 2
while divisor<number: 
    reminder = number % divisor
    if reminder == 0:
        print("it is not prime number")
        sys.exit(1)
    else:
        divisor = divisor + 1 

print("it is prime number")