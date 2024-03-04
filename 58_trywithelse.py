try:
    n1=int(input("Enter 1st number: "))
    n2=int(input("Enter 2nd number: "))
    div=n1/n2
    print(f"{n1}/{n2} = {div}")
except ZeroDivisionError:
    print(f"{n1}/{n2} is undefined.")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Program ended successflly.")