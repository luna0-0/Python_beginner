def convert(m):
    return m*100

meter=int(input("Enter value in meter: "))
print(f"{meter}m = "+str(convert(meter))+"cm")