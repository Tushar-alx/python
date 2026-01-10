#Create a dictionary and calculate the average of all values.

stud_dict1 = {
    "Tushar" : 90,
    "Vishal" : 56,
    "Raj" : 67,
    "Mahesh" : 79,
    "Jay" : 34
}
avg_marks = sum(stud_dict1.values())/len(stud_dict1)
print("Average of Values : ",avg_marks)