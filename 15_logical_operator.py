num1 = int(input("Enter Value for num1 :"))
num2 = int(input("Enter Value for num2 : "))
num3 = int(input("Enter Value for num3 :"))

#and operator

result = num1 == num2 and num2 == num3
print(f"{result} = {num1} == {num2} and {num2} == {num3}") 

result = num1 != num2 and num2 != num3
print(f"{result} = {num1} != {num2} and {num2} != {num3}") 

result = num1 < num2 and num2 < num3
print(f"{result} = {num1} < {num2} and {num2}< {num3}") 

result = num1 < num2 and num2 > num3
print(f"{result} = {num1} < {num2} and {num2}> {num3}") 

#or operator

result = num1 == num2 or num2 == num3
print(f"{result} = {num1} == {num2} and {num2} == {num3}") 

result = num1 != num2 or num2 != num3
print(f"{result} = {num1} != {num2} and {num2} != {num3}") 

result = num1 < num2 or num2 < num3
print(f"{result} = {num1} < {num2} and {num2}< {num3}") 

result = num1 < num2 or num2 > num3
print(f"{result} = {num1} < {num2} and {num2}> {num3}")

#not operator

result = not(num1 == num2 and num2 == num3)
print(f"{result} = {num1} == {num2} and {num2} == {num3}") 

result = not(num1 != num2 and num2 != num3)
print(f"{result} = {num1} != {num2} and {num2} != {num3}") 

result = not(num1 < num2 and num2 < num3)
print(f"{result} = {num1} < {num2} and {num2} < {num3}") 

result = not(num1 < num2 and num2 > num3)
print(f"{result} = {num1} < {num2} and {num2} > {num3}") 
