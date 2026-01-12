# write a program to findout name of cricketer in string which has 20 player name using in operator.

cricketers = "Sachin Tendulkar Virat Kohli MS Dhoni Rohit Sharma Jasprit Bumrah Hardik Pandya Rishabh Pant Shikhar Dhawan KL Rahul Yuzvendra Chahal Ravindra Jadeja Bhuvneshwar Kumar Ajinkya Rahane Dinesh Karthik Suresh Raina Kedar Jadhav Ishant Sharma Umesh Yadav Mohammed Shami Navdeep Saini"

name = input("Enter the name of cricketer to search: ")

print(name," is in string : ",name in cricketers)