x=20
def lscope():
    x=40
    print(f"Local scope: {x}")
    def escope():
        x=60
        print(f"Enclosing scope: {x}")
    escope()
lscope()
print(f"Global scope: {x}")