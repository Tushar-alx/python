'''
1 2 3 4 5  
1 2 3 4  
1 2 3  
1 2  
1
'''

for i in range(5,0,-1):
    n=1
    for j in range(i,0,-1):
        print(n,end=" ")
        n=n+1
    print("")