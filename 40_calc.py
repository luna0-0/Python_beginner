import math
class calculator():
    def sqr(self,a):
        print(f"Square of {a} = {a**2}")
    def cube(self,b):
        print(f"Cube of {b} = {b**3}")
    def sqrot(self,c):
        print(f"Square root of {c} = {math.sqrt(c)}")
    @staticmethod
    def greet():
        print("Hello!!")

square=calculator()
square.sqr(15)

cube=calculator()
cube.cube(5)

squareroot=calculator()
squareroot.sqrot(16)

g=calculator()
g.greet()