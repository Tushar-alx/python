# write a program to convert all negative values into positive values in the same list 

numbers = [-10, 20, -30, 40, -50, 60, -70]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = -numbers[i]
print(numbers)