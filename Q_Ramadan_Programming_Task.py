s=input()
ch=[]
for i in s:
    if i not in ["A","O","Y","E","U","I","a","o","y","e","u","i"]:
        ch.append(i.lower())
print("."+".".join(ch))