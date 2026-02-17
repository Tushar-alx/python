# write a program to figure out hexadcimal of given decimal number using recursion

def decimalToHexadecimal(n):
    if n == 0:
        return ""
    else:
        hex_digits = "0123456789ABCDEF"
        return decimalToHexadecimal(n // 16) + hex_digits[n % 16]
decimal_number = int(input("Enter a decimal number: "))
hexadecimal_number = decimalToHexadecimal(decimal_number)
print(f"The hexadecimal representation of {decimal_number} is {hexadecimal_number}")