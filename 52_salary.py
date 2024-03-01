class Employee():
    salary=1000
    inc=2
    @property
    def salaftinc(self):
        return self.salary*self.inc
    @salaftinc.setter
    def vinc(self,v):
        self.inc=v/self.salary
        return self.inc

e=Employee()
print(e.salaftinc)
e.vinc=1600
print(e.inc)