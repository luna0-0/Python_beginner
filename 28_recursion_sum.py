def add(n):
    if n==0 or n==1:
        return 1
    return n+add(n-1)
n=int(input("Enter a number: "))
print(f"Sum upto {n} natural numbers is: {add(n)}")