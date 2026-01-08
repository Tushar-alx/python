#Create a program to Enter any Two Digit Number and Display in Words.

num = input("Enter Two Digit Number : ")
num = int(num) 
 
first = num//10
last = num%10 

list = ['zero','one','two','three','four','five','six','seven','eight','nine']

print(list[first]," ",list[last])