#Write a program to convert seconds into minutes.

seconds = int(input("Enter time in seconds: "))

minutes = seconds // 60
remaining_seconds = seconds % 60

print(seconds, "seconds = ", minutes, "minutes and", remaining_seconds, "seconds")