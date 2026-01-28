# write a program to count odd and even number in numeric list 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_count = 0
even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print("Odd numbers:", odd_count)
print("Even numbers:", even_count)