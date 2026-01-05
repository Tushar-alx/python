places =['Ahmedabad','Bhavnagar','Surat','Jamnagar','Bhavnagar','Rajkot','Bhavnagar']
 
print(places)
 #inserting new Item in First Position
places.insert(0,'Dwarka')
print(places)
 
 #inserting new Item in Last Position
places.append('Gandhinagar')
print(places)
 
 #Find Index number of given Item
print(places.index('Surat'))

#find out how many items are there in list
print(places.count('Bhavnagar'))
 
 #Remove Item from list 
places.remove('Jamnagar')
print(places)

#Remove item from given index
places.pop(2)
print(places)
 
 #copy one list into another 
places2=places.copy()
print(places2)
 
#concatenate two lists
places.extend(places2)
print(places)

 #Remove all items from list
places2.clear()
print(places2)

 #delete entire list 
del places2