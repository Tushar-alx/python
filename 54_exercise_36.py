#Write a program to calculate the total price of items.

item_1 = int(input("Enter price of the first item: "))
item_2 = int(input("Enter price of the second item: "))
item_3 = int(input("Enter price of the third item: "))
item_4 = int(input("Enter price of the fourth item: "))
item_5 = int(input("Enter price of the fifth item: "))

items = [item_1, item_2, item_3, item_4, item_5]

total_price = sum(items)

print("The total price of items is:", total_price)
