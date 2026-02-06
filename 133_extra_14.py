'''

        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
'''

n = 5

for i in range(1, n + 1):
    # print leading spaces
    print("  " * (n - i), end="")
    
    # print numbers
    for j in range(2 * i - 1):
        print(i, end=" ")
    
    print()