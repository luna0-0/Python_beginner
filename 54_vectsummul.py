class vector():
    def __init__(self, vec):
        self.vec=vec

    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1+=f" {i}a{index} +"
            index +=1
            return str[:-1]

    def __add__(self, vec2):
        newlist=[]
        for i in range(len(self.vec2.vec)):
            newlist.append(self.vec[i]+vec2.vec[i])
        return vector(newlist)
        
v1=vector([2,4])
v2=vector([5,8])
print(v1+v2)