def convert(C):
    F=(C * 9/5) + 32
    return F
C=int(input("Celcius="))
print(f"{C} Celcius into Fahrenheit is: ",convert(C))