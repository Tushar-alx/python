'''
* * * * * 
*   *   *
* * * * *
*   *   *
* * * * *
'''
n = int(input("Enter an odd number (>=5): "))

if n < 5 or n % 2 == 0:
    print("Please enter an odd number greater than or equal to 5")
else:
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if (
                i == 0 or i == n - 1 or      # top & bottom border
                j == 0 or j == n - 1 or      # left & right border
                i == mid or j == mid         # middle row & column
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
