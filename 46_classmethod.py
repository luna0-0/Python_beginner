class employee():
    salary=15000
    @classmethod
    def change_s(cls, s):
        cls.salary=s
    
e=employee()
print(e.salary)
e.change_s(16000)
print(e.salary)
