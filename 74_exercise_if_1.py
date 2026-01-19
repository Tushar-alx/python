# write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. 

time = int(input("Enter Time : "))

#time must be between 0 to 23
if time==0:
        print("12 AM")
if time>0 and time<=23:  
    if time<12:
        print(time," AM")
    if time==12:
        print("12 PM")
    if time>12:
        print(time-12," PM")
if time<0 or time>23:
    print("Invalid time")