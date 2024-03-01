class complex():
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return complex(self.real+c.real, self.imaginary+c.imaginary)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __mul__(self,m):
        mul_real=self.real*m.real-self.imaginary*m.imaginary
        mul_img=self.real*m.imaginary+self.imaginary+m.real
        return complex(mul_real, mul_img)
    def __str__(self):
        return f"{self.real} * {self.imaginary}i"
c1=complex(3,2)
c2=complex(1,7)
print(c1+c2)
print(c1*c2)