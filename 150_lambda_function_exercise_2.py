#write a program to calculate fahrenheit of given celsius using lambda function 

celsius = float(input("Enter the temperature in Celsius: "))

fahrenheit = lambda c: (c * 9/5) + 32
result = fahrenheit(celsius)

print(f"The temperature in Fahrenheit is: {result:.2f}")