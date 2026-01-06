#Creating a dictionary
person = {'name':'Tushar Solanki','age':19,'weight':49,'gender':'Male','isMarried':False}

#display dictionary
print(person)

#access value using key
print(person['name']) 

#modify value using key
person['name'] = "Solanki Tushar"

#we can add new key value pair using assignment
person['city'] = 'Delhi'
person['pincode'] = 364001

#delete key value pair using del
del person['isMarried']
print(person)