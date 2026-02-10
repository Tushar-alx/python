'''
    *
  *   *
*       *
  *   *
    *
 
'''

n = int(input("Enter an odd number (>=5): "))

if n < 5 or n % 2 == 0:
    print("Please enter an odd number greater than or equal to 5")
else:
    mid = n // 2

    # Upper half (including middle row)
    for i in range(mid + 1):
        for j in range(n):
            if j == mid - i or j == mid + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Lower half
    for i in range(mid - 1, -1, -1):
        for j in range(n):
            if j == mid - i or j == mid + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()


 