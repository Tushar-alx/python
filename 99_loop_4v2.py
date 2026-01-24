#write a program to figure out whether given number is prime number or not 

import sys 
number = int(input("Enter number"))  
if number%2==0:
    print("it is not prime number")
else:
    divisor = 2
    half = (number // 2)  + 1
    while divisor<=half: 
        reminder = number % divisor
        if reminder == 0:
            print("it is not prime number")
            sys.exit(1) 
        else:
            divisor += 1 

    print("it is prime number")