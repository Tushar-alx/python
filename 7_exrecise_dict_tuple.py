#Excercise of Tulple

indian_states = (
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
)
#display Tuple
print(indian_states)

#display 1st five items
print(indian_states[0:5])

#display 2nd and 3rd and 4th item
print(indian_states[2:5])

#display all items from 7th position onwards
print(indian_states[7:])

#Remove 3rd item
# del indian_states[2] Error 

#Excercise of Dictionary

#create dictionary to store 20 details about ownself 

details = {
"Name":"Tushar",
"Surname":"Solanki",
"Address":"Airport Road",
"City":"Bhavnagar",
"State":"Gujarat",
"Country":"India",
"College":"SSCCS",
"Course":"BCA",
"Semester":6,
"Ismarried":False,
"Age":19,
"Gender":"Male",
"Height":168,
"Wight":49,
"Language":["Gujarati","Hindi","English"],
"DOB":"13-12-2006",
"Fav_color":"Red",
"Hobbies":"Playing Games",
"Passion":"Karate",
"Fav_fruit":"Apple"
}

#print Dictionary
print(details)

#print name, age, gender, dob
print(details['Name'],details['Age'],details['Gender'],details['DOB'])

#add key value pair pincode into dictionary
details['Pincode']=364001

#add key value pair to store your 5 favourite touriest destination

details['Fav_destination']=["Rajasthan","Dwarka","Goa","Mumbai","Delhi"]

#print all favourite touriest destination
print(details["Fav_destination"])