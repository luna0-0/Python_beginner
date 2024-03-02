class vector():
    def __init__(self, v):
        self.v=v
    def __str__(self):
        str2=""
        index=0
        for i in self.v:
            str2+=f"{i}a{index} + "
            index+=1
        return str2[:-2]

    def __len__(self, v2):
        if len(self.v)!=len(v2.v):
            print("Enter equal dimansion vectors")

    def __add__(self,v2):
        sum=[]
        for i in range(len(self.v)):
            sum.append(self.v[i]+v2.v[i])
        return sum

    def __mul__(self,v2):
        mult=0
        for i in range(len(self.v)):
            mult+=self.v[i]*v2.v[i]
        return mult

    def __len__(self):
        return len(self.v)

v=vector([1,8,4])
print(str(v))
v2=vector([5,9,0,7])
print(str(v2))
print(v+v2)
print(v*v2)
print(len(v))
print(len(v2))