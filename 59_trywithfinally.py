try:
    n=int(input("Enter a number: "))
    a=100*n
    print(a)
except Exception as e:
    print(e)
finally:
    print("Made with Python.")