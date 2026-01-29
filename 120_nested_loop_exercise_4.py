'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''

for i in range(5,0,-1):
    n=5
    for j in range(i,0,-1):
        print(n,end=" ")
        n=n-1
    print("")