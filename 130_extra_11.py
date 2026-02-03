'''
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
'''

for i in range(1,6):
    for k in range(5-i):
        print(" ",end=" ")
    n=1
    for j in range(i,0,-1):
        print(j,end=" ")
        n=n+1
    for j in range(2,i+1):
        print(j,end=" ")
    print("")
