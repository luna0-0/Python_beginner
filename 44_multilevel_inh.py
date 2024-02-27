class grandfather():
    def gname(self,name):
        self.name=name
        print(f"GrandFather's name is: {self.name}")

class father(grandfather):
    def fname(self,name):
        self.name=name
        print(f"Father's name is: {self.name}")

class son(father):
    def sname(self, name):
        self.name=name
        print(f"son's name is: {self.name}")

s=son()
s.gname('Hari')
s.fname('Ram')
s.sname('Rohan')