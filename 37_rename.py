import os
with open("12 File Handling/37 name.txt",'r') as f:
    file=f.read()
with open("12 File Handling/37 rename.txt",'w') as f:
    f.write(file)

os.remove("12 File Handling/37 name.txt")