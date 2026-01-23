# write a program to print following series 
# 1    -8   27  -64  .....    1000

number = 1
cube = 0
while abs(cube) < 1000:
     cube = number ** 3
     if number % 2 == 0:
          cube = 0 - cube
     print(cube, end=' ')
     number += 1
