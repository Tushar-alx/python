#write a program to accept day of week (between 1 to 7) and then display name of day. (use simple if decision making)

day = int(input("Enter day number (1-7): "))

if day==1:
    print("Monday")
if day==2:
    print("Tuesday")
if day==3:
    print("Wednesday")
if day==4:
    print("Thursday")
if day==5:
    print("Friday")
if day==6:
    print("Saturday")
if day==7:
    print("Sunday")
if day<1 or day>7:
    print("Invalid day number")