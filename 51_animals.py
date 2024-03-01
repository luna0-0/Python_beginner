class Animal():
    animaltype="Mammal"
    def type(self):
        print(f"Animial is {self.animaltype}.")

class pet(Animal):
    name="Dog"
    def type(self):
        super().type()
        print(f"Pet is {self.name}.")

class dog(pet):
    n="Bull dog"
    def type(self):
        super().type()
        print(f"Dog is {self.n}.")

a=dog()
a.type()