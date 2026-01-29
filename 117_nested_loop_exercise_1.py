'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

for i in range(1,6):
    n=1
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print("")