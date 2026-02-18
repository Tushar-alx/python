'''create module currency.py which has below methods 
    toDollar which convert given Rupees into Dollar 
    toEuro  which convert given Rupees into Euro 
    toPound which convert given Rupees into Pound 
    ToYen which convert given Rupees into Yen
'''
def toDollar(rupees):
    return rupees * 0.013
def toEuro(rupees):
    return rupees * 0.012
def toPound(rupees):
    return rupees * 0.011
def toYen(rupees):
    return rupees * 1.53

'''rupees = float(input("Enter the amount in Rupees: "))
print(f"{rupees} Rupees is equal to {toDollar(rupees):.2f} Dollars")
print(f"{rupees} Rupees is equal to {toEuro(rupees):.2f} Euros")
print(f"{rupees} Rupees is equal to {toPound(rupees):.2f} Pounds")
print(f"{rupees} Rupees is equal to {toYen(rupees):.2f} Yen")
'''