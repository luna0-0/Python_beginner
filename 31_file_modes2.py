f=open('31 file.txt','w')
text=f.write("This is mode write of the file.")
f.close()

f=open('31 file.txt','a')
text=f.write("\nThis line is added using append.")
f.close()