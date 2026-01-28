#write a program to count vowels, consonants, digits, words, and symbol in given list 

line = input("Enter a string: ")
vowel_count = 0
consonant_count = 0
digit_count = 0
word_count = 1
symbol_count = 0
for char in line:
    if char>='A' and char<='Z' or char>='a' and char<='z':
        if  char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
            vowel_count += 1
        else:
            consonant_count += 1
    elif char>='0' and char<='9':
        digit_count += 1
    elif char==' ':
        word_count += 1
    else:
        symbol_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("Words:", word_count)
print("Symbols:", symbol_count)
