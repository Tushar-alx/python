#write a program to findout whether particular key/value exist in dictionary or not using in operator 

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Check for key existence
key = input("Enter the key to check: ")

print(key," is in Dictionary : ",key in my_dict)

# Check for value existence
value = int(input("Enter the value to check: "))

print(value," is in Dictionary : ",value in my_dict.values())