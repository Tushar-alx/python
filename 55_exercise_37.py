#Write a program to calculate discount amount using price and discount rate.

price = int(input("Enter the price of the item: "))
discount_rate = float(input("Enter the discount rate (in percentage): "))

discount_amount = (discount_rate / 100) * price
print("Discount Amount:", discount_amount)

final_price = price - discount_amount
print("Final Price:", final_price)