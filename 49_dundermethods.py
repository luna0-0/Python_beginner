class number():
    def __init__(self,num):
        self.num=num
    def __str__(self):
        return f"Decimal number: {self.num}"
    def __len__(self):
        return 1

n=number(95)
print(n)
print(len(n))