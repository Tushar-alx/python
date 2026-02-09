'''
A 
B C
D E F
G H I J
K L M N O
P Q R S T U
'''

n = 6
count = 65
for i in range(n):
    for j in range(i + 1):
        print(chr(count), end=' ')
        count += 1
    print()