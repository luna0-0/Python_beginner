# Program to print reverse of mutiplication table of n 
n=int(input("Number: "))
m=[]
for i in range(1,11):
    m.append(f"{n}*{i}={n*i}")

m.reverse()
for j in m:
    print(j)
        