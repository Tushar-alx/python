# write a program to display 1 to 10 in reverse order using recursion

def printNumber(number):
    if number>=1:
        print(number)
        number=number-1
        printNumber(number)  

number = 10 
printNumber(number)