#create Dictionary
person = {'name':'Tushar Solanki','age':19,'weight':49,'gender':'Male','isMarried':False}

#print dictionary
print(person)

#access all keys
print("Keys:", person.keys())

#access all values
print("Values:", person.values())

#access all key-value pairs
print("Items:", person.items())

#access specific value using get()
print("Name:", person.get('name'))

#update dictionary
person.update({'city': 'Delhi', 'pincode': 364001})
print("Updated Dictionary:", person)

#remove a key-value pair
removed_value = person.pop('isMarried')
print("Removed Value:", removed_value)
print("Dictionary after pop():", person)

#remove last key-value pair
last_item = person.popitem()
print("Last Item:", last_item)
print("Dictionary after popitem():", person)

#copy the dictionary
person_copy = person.copy()
print("Copied Dictionary:", person_copy)

#create a new dictionary from keys and values using fromkeys()
keys = ['a', 'b', 'c']
values = [1, 2, 3]
new_dict = dict.fromkeys(keys, values)
print("New Dictionary from fromkeys():", new_dict)

#clear the dictionary
person.clear()
print("Cleared Dictionary:", person)