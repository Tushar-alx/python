'''
        1
       1 1
      1 2 1 
     1 3 3 1
    1 4 6 4 1
'''   
 
for i in range(1,6):
    for k in range(5-i):
        print(" ",end=" ")
    n=1
    for j in range(1,i+1):
        print(n,end="   ")
        n=n*(i-j)//j
    print("")