'''write a program to findout day of week(monday/tuesday/wednesday) from given date.  
   https://www.wikihow.com/Calculate-the-Day-of-the-Week 
'''

day = int(input("Enter day (1-31): "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year (YYYY): "))

if month < 3:
    month += 12
    year -= 1

k = year % 100
j = year // 100
f = day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j)
day_of_week = f % 7

if day_of_week == 0:
    print("Saturday")
elif day_of_week == 1:
    print("Sunday")
elif day_of_week == 2:
    print("Monday")
elif day_of_week == 3:
    print("Tuesday")
elif day_of_week == 4:
    print("Wednesday")
elif day_of_week == 5:
    print("Thursday")
elif day_of_week == 6:
    print("Friday")
else:
    print("Invalid date")