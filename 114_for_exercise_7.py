#write a program to findout coutries whose area is greater given area. use chatgpt to create dictionaries which country name as key and its' area as value. 

countries_area = {
    'Russia': 17098242,
    'Canada': 9984670,
    'China': 9596961,
    'United States': 9372610,
    'Brazil': 8515767,
    'India': 3287263,
    'Australia': 7692024,
    'Germany': 357578,
    'France': 551695,
    'United Kingdom': 243610,
}   
given_area = int(input("Enter the area to compare (in square kilometers): "))
print("Countries with area greater than", given_area, "square kilometers:")
for country, area in countries_area.items():
    if area > given_area:
        print(country)
        