#write a program to create function that calculate and return simple interest of given amount rate and year 

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

principal = float(input("Enter principal amount: "))
if(principal < 0):
    print("Principal amount cannot be negative.")
    exit(1)
rate = float(input("Enter rate of interest: "))
if(rate < 0):
    print("Rate of interest cannot be negative.")
    exit(1)
time = float(input("Enter time in years: "))
if(time < 0):
    print("Time cannot be negative.")
    exit(1)

interest = simple_interest(principal, rate, time)

print(f"Simple Interest: {interest}")