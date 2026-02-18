#write a program to convert list that has mixed case countries names into lowercase countries name using lambda

countries = ["India", "United States", "Germany", "France", "Japan"]

lowercase_countries = list(map(lambda x: x.lower(), countries))

print(lowercase_countries)