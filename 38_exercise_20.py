#Given two lists, convert them into sets and find common elements.

list1 = [1,2,3,4,5]
list2 = [1,3,5,7,9]

set1 = set(list1)
set2 = set(list2)

print("Common Elements : ",set1.intersection(set2))