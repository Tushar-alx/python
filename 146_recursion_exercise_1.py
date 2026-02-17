#write a program to figure out octal of given decimal number using recursion

def decimalToOctal(n):
    if n == 0:
        return 0
    else:
        return (n % 8) + 10 * decimalToOctal(n // 8)
decimal_number = int(input("Enter a decimal number: "))
octal_number = decimalToOctal(decimal_number)
print(f"The octal representation of {decimal_number} is {octal_number}")