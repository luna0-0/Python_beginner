class c2dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def  __str__(self):
        return f"{self.icap}i+{self.jcap}j"

class c3dvec:
    def __init__(self,i,j,k):
        self.icap=i
        self.jcap=j
        self.kcap=k

    def  __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"

v2d=c2dvec(7,9)
print(v2d)
v3d=c3dvec(2,5,6)
print(v3d)