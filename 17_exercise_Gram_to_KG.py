#Excersise: Convert Grams into Kilograms and Grams
gram = int(input("Enter grams : "))

kg = gram//1000
gram = gram%1000

print(kg," Kilogram ",gram," Grams")