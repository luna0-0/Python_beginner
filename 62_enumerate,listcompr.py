list=[8,9,0.6,'hello']
for index,i in enumerate(list):
    print(index,i)
print()

s={3,5,6,3,'a','a',7.8}
for i,e in enumerate(s):
    print(i,e)
print()

# List Comprehensions
l1=[20,4,63,45,11,9,0]
l2=[i for i in l1 if i>=20]
print(l2)