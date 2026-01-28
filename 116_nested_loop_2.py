'''
* * * * *
* * * *
* * *
* *
*
'''

count = int(input("Enter Number : "))
for row in range(count+1,1,-1):
    for astrik in range(1,row):
        print("*",end=' ')
    print("")