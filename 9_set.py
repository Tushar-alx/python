#create a set
fruits = {'apple', 'banana', 'cherry', 'date'}

#print the set
print("Fruits Set:", fruits)

#add an element to the set
fruits.add('berry')
print("Updated Fruits Set:", fruits)

#try to add a duplicate element
fruits.add('apple')
print("After Adding Duplicate, Fruits Set:", fruits)

#remove an element from the set
fruits.remove('date')
print("Updated Fruits Set:", fruits)    

#update the set with multiple elements
fruits.update(['kiwi', 'mango', 'orange'])
print("Updated Fruits Set:", fruits)

#clear the set
fruits.clear()
print("Cleared Fruits Set:", fruits)    

#Set operations
a={1,2,3,4,5}
b={4,5,6,7,8}

#union of sets
print("Union:", a.union(b))

#intersection of sets
print("Intersection:", a.intersection(b))

#difference of sets
print("Difference:", a.difference(b))