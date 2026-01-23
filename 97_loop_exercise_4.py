# write number1 progrnumber1m to print following series 
# 0    1   1   2   3   5   8   13  .... 100

sum = 0
number1=0
number2=1

while sum <= 100:
    print(sum, end=' ')
    number1=number2
    number2=sum
    sum=number1+number2