'''write a program display marriage compatibility for male female using birth dates as per below link,  accept birth day and birth month from user as separate input for both male & female. decide zodiac sign as per previous example and then use zodiac sign to decide  marriage compatibility
https://miro.medium.com/v2/resize:fit:1100/format:webp/1*f58HMTVzfN2XvCPR23wXgA.jpeg
'''

male_day = int(input("Enter male birth day (1-31): "))
male_month = int(input("Enter male birth month (1-12): "))

if male_month == 3 and male_day >= 21 or male_month == 4 and male_day <= 19:
    male_zodiac_sign = "Aries"
elif male_month == 4 and male_day >= 20 or male_month == 5 and male_day <= 20:
    male_zodiac_sign = "Taurus"
elif male_month == 5 and male_day >= 21 or male_month == 6 and male_day <= 21:
    male_zodiac_sign = "Gemini"
elif male_month == 6 and male_day >= 22 or male_month == 7 and male_day <= 22:
    male_zodiac_sign = "Cancer"
elif male_month == 7 and male_day >= 23 or male_month == 8 and male_day <= 22:
    male_zodiac_sign = "Leo"
elif male_month == 8 and male_day >= 23 or male_month == 9 and male_day <= 22:
    male_zodiac_sign = "Virgo"
elif male_month == 9 and male_day >= 23 or male_month == 10 and male_day <= 22:
    male_zodiac_sign = "Libra"
elif male_month == 10 and male_day >= 24 or male_month == 11 and male_day <= 21:
    male_zodiac_sign = "Scorpio"
elif male_month == 11 and male_day >= 22 or male_month == 12 and male_day <= 21:
    male_zodiac_sign = "Sagittarius"
elif male_month == 12 and male_day >= 22 or male_month == 1 and male_day <= 19:
    male_zodiac_sign = "Capricorn"
elif male_month == 1 and male_day >= 20 or male_month == 2 and male_day <= 18:
    male_zodiac_sign = "Aquarius"
elif male_month == 2 and male_day >= 19 or male_month == 3 and male_day <= 20:
    male_zodiac_sign = "Pisces"
else:
    print("Invalid birth date")

female_day = int(input("Enter female birth day (1-31): "))
female_month = int(input("Enter female birth month (1-12): "))

if female_month == 3 and female_day >= 21 or female_month == 4 and female_day <= 19:
    female_zodiac_sign = "Aries"
elif female_month == 4 and female_day >= 20 or female_month == 5 and female_day <= 20:
    female_zodiac_sign = "Taurus"
elif female_month == 5 and female_day >= 21 or female_month == 6 and female_day <= 21:
    female_zodiac_sign = "Gemini"
elif female_month == 6 and female_day >= 22 or female_month == 7 and female_day <= 22:
    female_zodiac_sign = "Cancer"
elif female_month == 7 and female_day >= 23 or female_month == 8 and female_day <= 22:
    female_zodiac_sign = "Leo"
elif female_month == 8 and female_day >= 23 or female_month == 9 and female_day <= 22:
    female_zodiac_sign = "Virgo"
elif female_month == 9 and female_day >= 23 or female_month == 10 and female_day <= 22:
    female_zodiac_sign = "Libra"
elif female_month == 10 and female_day >= 24 or female_month == 11 and female_day <= 21:
    female_zodiac_sign = "Scorpio"
elif female_month == 11 and female_day >= 22 or female_month == 12 and female_day <= 21:
    female_zodiac_sign = "Sagittarius"
elif female_month == 12 and female_day >= 22 or female_month == 1 and female_day <= 19:
    female_zodiac_sign = "Capricorn"
elif female_month == 1 and female_day >= 20 or female_month == 2 and female_day <= 18:
    female_zodiac_sign = "Aquarius"
elif female_month == 2 and female_day >= 19 or female_month == 3 and female_day <= 20:
    female_zodiac_sign = "Pisces"
else:
     print("Invalid birth date")


zodiac_sign = {
    "Aries": 1,
    "Leo": 2,
    "Sagittarius": 3,
    "Taurus": 4,
    "Virgo": 5,
    "Capricorn": 6,
    "Gemini": 7,
    "Libra": 8,
    "Aquarius": 9,
    "Cancer": 10,
    "Scorpio": 11,
    "Pisces": 12
}


print("Male Zodiac Sign:", male_zodiac_sign)
print(zodiac_sign[male_zodiac_sign])
print("Female Zodiac Sign:", female_zodiac_sign)
print(zodiac_sign[female_zodiac_sign])    

#--------- Great Match Logic ---------------
if zodiac_sign[male_zodiac_sign]==1 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==3\
     or zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==8 or zodiac_sign[female_zodiac_sign]==9):
    print("Great Match")

elif zodiac_sign[male_zodiac_sign]==2 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==3\
        or zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==8):
    print("Great Match")  

elif zodiac_sign[male_zodiac_sign]==3 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==3\
        or zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==8 or zodiac_sign[female_zodiac_sign]==9):
    print("Great Match")

elif zodiac_sign[male_zodiac_sign]==4 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6\
        or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11 or zodiac_sign[female_zodiac_sign]==12):
    print("Great Match")

elif zodiac_sign[male_zodiac_sign]==5 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6\
        or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11):
    print("Great Match")

elif zodiac_sign[male_zodiac_sign]==6 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6\
        or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11 or zodiac_sign[female_zodiac_sign]==12):
    print("Great Match")

elif zodiac_sign[male_zodiac_sign]==7 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==7\
        or zodiac_sign[female_zodiac_sign]==8 or zodiac_sign[female_zodiac_sign]==9):
    print("Great Match")

elif zodiac_sign[male_zodiac_sign]==8 and (zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==3 or zodiac_sign[female_zodiac_sign]==7\
        or zodiac_sign[female_zodiac_sign]==8 or zodiac_sign[female_zodiac_sign]==9):
    print("Great Match")

elif zodiac_sign[male_zodiac_sign]==9 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==3\
        or zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==8 or zodiac_sign[female_zodiac_sign]==9):
    print("Great Match")

elif zodiac_sign[male_zodiac_sign]==10 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6\
        or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11 or zodiac_sign[female_zodiac_sign]==12):
    print("Great Match")


elif zodiac_sign[male_zodiac_sign]==11 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6\
        or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11 or zodiac_sign[female_zodiac_sign]==12):
    print("Great Match")


elif zodiac_sign[male_zodiac_sign]==12 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==6\
        or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11 or zodiac_sign[female_zodiac_sign]==12):
    print("Great Match")

#---------Favorable Match Logic ---------------

if zodiac_sign[male_zodiac_sign]==1 and (zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==12):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==2 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]== 9 or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11 or zodiac_sign[female_zodiac_sign]==12):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==3 and (zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11 or zodiac_sign[female_zodiac_sign]==12):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==4 and (zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==8):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==5 and (zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==9 or zodiac_sign[female_zodiac_sign]==12):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==6 and (zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==8):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==7 and (zodiac_sign[female_zodiac_sign]==3 or zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==8 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==12):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==9 and (zodiac_sign[female_zodiac_sign]==11 or zodiac_sign[female_zodiac_sign]==12):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==10 and (zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==3):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==11 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==2):
    print("Favorable Match")
elif zodiac_sign[male_zodiac_sign]==12 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==2 or zodiac_sign[female_zodiac_sign]==3 or zodiac_sign[female_zodiac_sign]==5):
    print("Favorable Match")

#--------- Not Favourable Logic ---------------    

if zodiac_sign[male_zodiac_sign]==1 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==6 or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11):
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==2 and (zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6):
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==3 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6):
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==4 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==3 or zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==9):
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==5 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==3 or zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==8):
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==6 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==3 or zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==9):
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==7 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11 or zodiac_sign[female_zodiac_sign]==12):  
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==8 and (zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6 or zodiac_sign[female_zodiac_sign]==10 or zodiac_sign[female_zodiac_sign]==11):  
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==9 and (zodiac_sign[female_zodiac_sign]==4 or zodiac_sign[female_zodiac_sign]==5 or zodiac_sign[female_zodiac_sign]==6 or zodiac_sign[female_zodiac_sign]==10):
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==10 and (zodiac_sign[female_zodiac_sign]==1 or zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==8 or zodiac_sign[female_zodiac_sign]==9):
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==11 and (zodiac_sign[female_zodiac_sign]==3 or zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==8 or zodiac_sign[female_zodiac_sign]==9):
    print("Not Favourable Match")
elif zodiac_sign[male_zodiac_sign]==12 and (zodiac_sign[female_zodiac_sign]==7 or zodiac_sign[female_zodiac_sign]==8 or zodiac_sign[female_zodiac_sign]==9):
    print("Not Favourable Match")
 