c=int(input("Marks in CS: "))
e=int(input("Marks in English: "))
m=int(input("Marks in Math: "))
t=(c+e+m)/3
if(c<33 or e<33 or m<33):
        print("Fail")
elif(t<40):
    print("Fail")
else:
    print("Pass")