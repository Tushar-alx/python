# write a program to figure out binary of given decimal number 

def toBinary(number):
    if number>0:
        reminder = number % 2 
        number = number // 2 
        toBinary(number) 
        print(reminder,end=' ') 

number = int(input("Enter number : "))
toBinary(number) 