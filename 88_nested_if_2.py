# write a program to find out whether given year is leap year or not
# https://www.wikihow.com/Calculate-Leap-Years

year = int(input("Enter year")) 

if year<1:
    print("invalid year")
else:   
    if year%4==0 and year%100!=0:
        print("given year is leap year")
    else:
        if year%100==0 and year%400==0:
            print("given year is leap year")
        else:
            print("given year is not leap year")