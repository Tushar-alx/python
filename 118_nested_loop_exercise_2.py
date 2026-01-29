'''
1
0 1
0 1 0
1 0 1 0
1 0 1 0 1
'''
n=0
for i in range(1,6):
    for j in range(1,i+1):
        if (n)%2==0:
            print("1",end=" ")
            n=1
        else:
            print("0",end=" ")
            n=0
    print("")