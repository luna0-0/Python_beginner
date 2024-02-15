d={
    "hello": "namaste",
    "python": "programming",
    "list": [4,6,7,8,9],
    "Name":{"luna":"dahal"}
}
print(d["hello"])
print(d["Name"]["luna"])
d["list"]=[1,2,3,4,5]

# Methods
print(d.keys())
print(list(d.values()))
print(d.items())
d2={
    "list2":[3,1,5,7,5],
    "python":"language"
}
d.update(d2)
print(d)

print(d.get("Name"))
print(d["Name"])
print(d.get("name"))
