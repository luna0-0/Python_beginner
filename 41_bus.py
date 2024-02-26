class train():
    def __init__(self,s,f):
        print("Train ticket booking methods: ")
        print(f"Number of seats = {s}")
        print(f"Fare = Rs.{f}")
        if s >= 1:
            print("You have successfully booked a ticket.")
            print(f"Your seat number is: {s}")
            s=s-1
            print(f"Remaining seats = {s}")
        else:
            print("Sorry the trian is full.")

train(4,100)