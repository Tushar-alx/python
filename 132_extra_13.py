'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    num = i % 2   # starting value of each row

    for j in range(1, i + 1):
        print(num, end=" ")
        num = 1 - num   # toggle between 1 and 0

    print()