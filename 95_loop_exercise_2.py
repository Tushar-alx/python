# write a program to print following series 
# 1    8   27   125  ....... 1000

number = 1
cube = 0
while cube < 1000:
     cube = number ** 3
     print(cube, end=' ')
     number += 1

     