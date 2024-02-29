class Employee():
    salary=10000
    bonus=400

    @property
    def total_s(self):
        return self.salary+self.bonus
    
    @total_s.setter
    def total_s(self, v):
        self.bonus=v-self.salary

    
e=Employee()
print(e.total_s)
e.total_s=10800
print(e.total_s)
print(e.bonus)