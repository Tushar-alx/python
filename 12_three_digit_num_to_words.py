#Create a program to Enter any three Digit Number and Display in Words.

num = input("Enter Three Digit Number : ")
num = int(num) 
 
temp = num//10 
first = temp //10
mid = temp %10
last = num%10 

list = ['zero','one','two','three','four','five','six','seven','eight','nine']

print(list[first]," ",list[mid]," ",list[last])

