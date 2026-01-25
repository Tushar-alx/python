#write a program to figure out whether given number  is armstrong number or not

number = int(input("Enter number : ")) 
temp = number
sum = 0
while temp>0: 
    rem = temp % 10
    sum = sum + (rem ** 3)
    temp = temp // 10

if sum == number:
    print("it is armstrong number")
else:
    print("it is not armstrong number")