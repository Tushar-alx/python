#write a program to figure out whether given number  is composite number or not

number = int(input("Enter number : ")) 
divisor = 2
while divisor<number: 
    reminder = number % divisor
    if reminder == 0:
        print("it is composite number")
        break
    else:
        divisor = divisor + 1 

if divisor == number:
    print("it is not composite number")