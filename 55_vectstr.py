class vector():
    def __init__(self, v):
        self.v=v

    def __str__(self):
        vect=f"{self.v[0]}i + {self.v[1]}j + {self.v[2]}k"
        return vect
    
v=vector([2, 3, 5])
print(v)