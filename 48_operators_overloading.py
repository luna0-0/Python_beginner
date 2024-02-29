class Number():
    def __init__(self,num1):
        self.num1=num1
    def __add__(self,num2):
        print("Addition:")
        return self.num1+num2.num1
    def __mul__(self,num2):
        print("Multiplication:")
        return self.num1*num2.num1
    def __truediv__(self,num2):
        print("Division:")
        return self.num1/num2.num1
    def __floordiv__(self,num2):
        print("Floor Division:")
        return self.num1//num2.num1

n1=Number(25)
n2=Number(10)
sum=n1+n2
print(sum)
mul=n1*n2
print(mul)
div=n1/n2
print(div)
fd=n1//n2
print(fd)