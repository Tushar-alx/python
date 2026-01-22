# write a program to print following series 
# 1     -4      9     -16     25      -36  ...   1000
     
number = 1
square = 0
while square<961:
    square = number * number 
    reminder = number % 2 
    if reminder==0: 
        square = 0 - square
    print(square,end=' ')
    number += 1