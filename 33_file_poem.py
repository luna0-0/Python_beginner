f=open('33 poem.txt','r')
poem=f.read()
if 'twinkle' in poem:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()