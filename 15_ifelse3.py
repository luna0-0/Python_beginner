text=input("Enter text: ")
if("buy now" in text):
    spam=True
elif("subscribe" in text):
    spam=True
elif("make money" in text):
    spam=True
else:
    spam=False

if(spam==True):
    print("This is a spam")
else:
    print("This is not a spam")