class parent():
    def func(self):
        print("This is inside parent class")

class child(parent):
    def funct(self):
        print("This is inside child class")

c=child()
c.func()
c.funct()