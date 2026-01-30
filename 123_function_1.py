#Write a function to calculate square of a number and cube of a number 

def getSquare(number):
    square = number * number
    return square

def getcube(num):
    cube = getSquare(num) * num 
    return cube 

n1 = int(input("Enter number"))
result = getSquare(n1)  
print("Square = ",result)

result2 = getcube(n1)
print("cube = ",result2)