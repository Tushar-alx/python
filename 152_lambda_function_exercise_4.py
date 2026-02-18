#write a program to convert list that has mixed case countries names into uppercase countries name  using lambda

countries = ["India", "United States", "Germany", "France", "Japan"]

uppercase_countries = list(map(lambda x: x.upper(), countries))

print(uppercase_countries)