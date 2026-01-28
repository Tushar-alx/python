#2) write a program to generate and display sum of all the float values in tuple and also calculate average 

values = (10, 20.5, 30, 40.5, 50, 60.5)
sum_float = 0
count_float = 0

for value in values:
    if isinstance(value, float):
        sum_float += value
        count_float += 1

if count_float > 0:
    average_float = sum_float / count_float
    print("Sum of float values:", sum_float)
    print("Average of float values:", average_float)
else:
    print("No float values found in the tuple.")