class parent1():
    def func1(self):
        print("This is inside 1st parent class")

class parent2():
    def func2(self):
        print("This is inside 2nd parent class")

class child(parent1, parent2):
    def func3(self):
        print("This is a child class")

c=child()
c.func1()
c.func2()
c.func3()