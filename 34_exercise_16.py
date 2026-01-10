#Given a tuple of numbers, convert it into a list and add new elements.

tuple = (1,2,3,4,5,6,7)
print("Tuple : ",tuple)

list = list(tuple)
print("List : ",list)

num = int(input("Enter new element : "))
list.append(num)
print("List after adding new element : ",list)