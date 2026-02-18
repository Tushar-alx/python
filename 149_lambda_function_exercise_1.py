#write a program to calculate compound interest using lambda function 

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time in years: "))

compound_interest = lambda p, r, t: p * (1 + r / 100) ** t - p
result = compound_interest(principal, rate, time)

print(f"The compound interest is: {result:.2f}")
