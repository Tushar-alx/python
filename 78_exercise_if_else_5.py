#write a program to find out elder brother from given two brother's age. 

age1 = int(input("Enter 1st brother age : "))
age2 = int(input("Enter 2nd brother age : "))

# Check who is elder
if age1 > age2:
    print("First brother is elder")
else:
    if age2 > age1:
        print("Second brother is elder")
    else:
        print("Both brothers are of the same age")
