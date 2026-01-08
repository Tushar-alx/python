#Create a program to Enter any three Digit Number and Display in Words.

num = input("Enter Three Digit Number : ")
num = int(num) 
 
temp = num//10 
first = temp //10
mid = temp %10
last = num%10 

first_list = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eightty','ninety']
mid_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
last_list = ['zero','one','two','three','four','five','six','seven','eight','nine']

# print in words(for example 123 one hundred twenty three) 
if first!=0:
    print(last_list[first]," hundred ", end="")
if mid==1:
    print(mid_list[last])
if mid!=1:
    print(first_list[mid]," ", end="")
    print(last_list[last])