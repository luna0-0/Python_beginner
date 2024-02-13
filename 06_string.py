a=("30 Days Learning Challenge by: ")
b=input("Name: ")
c=a+b
print(c)

print(c[8:])
print(c[15:-5])
print(c[0:30:2]) #Escape 2 letters and print
print(c[4::3])

#String functions
print("Name length=",len(b))
print(c.endswith("na"))
print(c.count('n'))
print(b.capitalize())
print(c.find("Days"))
print(c.replace('Learning','Python'))