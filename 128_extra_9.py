#write a program to find number is plaindrome or not

from unicodedata import digit


num = int(input("Enter a number: "))
org = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

if org == rev:
    print(org, "is a palindrome number")
else:
    print(org, "is not a palindrome number")