'''write a program to accept 2 number from user. and accept choice for operations.
operations will be addition, subtraction, multiplication, division
do operation and display result as per user choice about operation using if elif else statements.
'''

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Enter 1 for addition \nEnter 2 for subtraction \nEnter 3 for multiplication \nEnter 4 for division: ")
choice = input("Enter your choice : ")

if choice == '1':
    result = num1 + num2
    print("Addition:", result)
elif choice == '2':
    result = num1 - num2
    print("Subtraction:", result)
elif choice == '3':
    result = num1 * num2
    print("Multiplication:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Division:", result)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid operation.")