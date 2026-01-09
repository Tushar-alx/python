#Excersise: Currency Denomination
curr = int(input("Enter Value of Currency : "))
 
n_500 = curr//500
temp = curr-(500*n_500)
print("500 x ",n_500)

n_200 = temp//200
temp = temp-(200*n_200)
print("200 x ",n_200)

n_100 = temp//100
temp = temp-(100*n_100)
print("100 x ",n_100)

n_50 = temp//50
temp = temp-(50*n_50)
print("50 x ",n_50)

n_20 = temp//20
temp = temp-(20*n_20)
print("20 x ",n_20)

n_10 = temp//10
temp = temp-(10*n_10)
print("10 x ",n_10)

n_5 = temp//5
temp = temp-(5*n_5)
print("5 x ",n_5)

n_2 = temp//2
temp = temp-(2*n_2)
print("2 x ",n_2)

n_1 = temp//1
temp = temp-(1*n_1)
print("1 x ",n_1)