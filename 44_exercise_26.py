#Write a program to calculate total amount after simple interest.

principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time period(in years): "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

total_amount = principal + simple_interest
print("Total Amount:", total_amount)