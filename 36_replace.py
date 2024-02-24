words=['twinkle','blazing','dark','peep']
with open("33 poem.txt") as f:
    text=f.read().lower()
for i in words:
    text=text.replace(i,"*#*@*$")

with open("33 poem.txt",'w') as f:
    f.write(text)
    print(text)

i=1
line=True
with open("33 poem.txt") as f:
    while line:
        line=f.readline()
        if 'little' in line:
            print(f"little is in line {i}")
        i+=1