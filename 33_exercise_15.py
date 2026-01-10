#Create a list of numbers and remove all duplicate values without using loops.

num_list = [1,2,3,4,5,6,7,8,9,10,2,3,4,7,6,5,8,1,10,1,2,1]

print("Original List : ",num_list)

unique_list = list(set(num_list))
print("List with Unique values : ",unique_list)