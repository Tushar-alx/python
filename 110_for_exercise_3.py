# write a program to count words in given string 

line = input("Enter a string: ")
word_count = 0
for char in line:
    if char == ' ':
        word_count += 1
word_count += 1
print("Number of words:", word_count)