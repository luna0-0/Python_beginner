def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n3):
        return n2
    else:
        return n3
n1=int(input("Number 1: "))
n2=int(input("Number 2: "))
n3=int(input("Number 3: "))
print(f"Greatest among {n1}, {n2} and {n3} is: ",greatest(n1,n2,n3))