#Create a list and find the second largest number using sorting.

num_list = [1,3,5,7,9,2,4,6,8,10]

num_list.sort()
sec_larg= len(num_list)
print("Second Largest Number : ",num_list[sec_larg-2])