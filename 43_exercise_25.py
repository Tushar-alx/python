#Write a program to calculate simple interest using principal, rate, and time.

principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time period(in years): "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)