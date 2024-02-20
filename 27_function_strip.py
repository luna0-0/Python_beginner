def strings(string,word):
    stri=string.replace(word,"")
    return stri.strip()

string="     Hello, World!!    "
print(strings(string,"World"))