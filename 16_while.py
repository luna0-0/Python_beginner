# Program to find sum of n natural numbers
n=int(input("Number: "))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print(f"Sum of {n} natural numbers={sum}")