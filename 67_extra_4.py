#Program to enter number of days and convert into year, month and days format.

day = int(input("Enter number of days : "))

year = day//365
temp = day%365
month = temp//30
day = temp%30

print(f"{year} Year {month} Month {day} Days")