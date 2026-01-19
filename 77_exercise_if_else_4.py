#write a program to find out whether given year is millennium year or not. using if else decision making statements.

year = int(input("Enter year : "))

if year%1000==0:
    print(year," is millennium year")
else:
    print(year," is not millennium year")