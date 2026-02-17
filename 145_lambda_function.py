# write a lambda function to calculate and return simple interest of given amount rate year 
 
getInterest = lambda amount, rate, year : (amount * rate * year ) / 100

amount = float(input("enter amount : "))
rate = float(input("enter rate : "))
year = float(input("enter year : "))

interest = getInterest(amount,rate,year)
print("Simple interest : ",interest)