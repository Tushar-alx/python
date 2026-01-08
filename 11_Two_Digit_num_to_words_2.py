#Create a program to Enter any Two Digit Number and Display in Words.

num = input("Enter Two Digit Number : ")
num = int(num) 
 
first = num//10
last = num%10 

first_list = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
mid_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
last_list = ['zero','one','two','three','four','five','six','seven','eight','nine']

if num<1 or num>99:
    print("Please Enter Valid Two Digit Number")
else:
    if first==1:
        print(mid_list[last])
    if first!=1:
        print(first_list[first]," ", end="")
        print(last_list[last])
 

 