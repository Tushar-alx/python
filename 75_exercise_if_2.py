#write a program to accept length and width of two different farm from user. and find out & display which farm is bigger

length1 = float(input("Enter 1st farm length"))
width1 = float(input("Enter 1st farm width"))

length2 = float(input("Enter 2nd farm length"))
width2 = float(input("Enter 2nd farm width"))

#calculate area of farm
area1 = length1 * width1
area2 = length2 * width2

if area1>area2:
    print("1st farm is bigger")
    
if area2>area1:
    print("2nd farm is bigger")