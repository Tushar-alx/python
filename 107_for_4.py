# write a program to count vowels from user given string
 
line = input("What is your name")

vowels = ['a','e','i','o','u']
count = 0

print("Vowels in your name are : ")

for letter in line:
     if str.lower(letter) in vowels:
          count+=1        
print(count)