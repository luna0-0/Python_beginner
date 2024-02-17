a=int(input("Enter Number 1: "))
b=int(input("Enter Number 2: "))
c=int(input("Enter Number 3: "))
d=int(input("Enter Number 4: "))
if(a>b and a>c and a>d):
    print(a," is greatest")
elif(b>c and b>d):
    print(b," is greatest")
elif(c>d):
    print(c," is greatest")
else:
    print(d," is greatest")
