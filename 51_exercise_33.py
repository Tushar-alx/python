#Write a program to calculate the average of marks.
 
sub_1 = int(input("Enter marks of the first subject: "))
sub_2 = int(input("Enter marks of the second subject: "))
sub_3 = int(input("Enter marks of the third subject: "))
sub_4 = int(input("Enter marks of the fourth subject: "))
sub_5 = int(input("Enter marks of the fifth subject: "))

marks = [sub_1, sub_2, sub_3, sub_4, sub_5]

average = sum(marks)/len(marks)

print("The average of marks is:", average)

