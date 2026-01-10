#Count how many times a specific value appears in a list using built-in methods.

#creating List 
num = [1,2,3,4,5,6,7,8,9,10,2,3,4,7,6,5,8,1,10,1,2,1]

#input of user
ch = int(input("Enter Value for Counting : "))

#Display number how many times appear in list
print(ch," is ",num.count(ch)," times in list")
