#Merge two dictionaries into a single dictionary.

stud_dict1 = {
    "Tushar" : 90,
    "Vishal" : 56,
    "Raj" : 67,
    "Mahesh" : 79,
    "Jay" : 34
}

stud_dict2 = {
    "Jayesh" : 55,
    "Gopal" : 44,
    "Ram" : 32,
}

stud_dict1.update(stud_dict2)
print("Combination of two dictionary : ",stud_dict1)