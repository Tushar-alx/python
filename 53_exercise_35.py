#Write a program to convert minutes into hours.

minutes = int(input("Enter time in minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(minutes, "minutes = ", hours, "hours and", remaining_minutes, "minutes")