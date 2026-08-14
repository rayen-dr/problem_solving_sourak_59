s=input()
ch="hello"
beg=0
for i in ch:
    ok=False
    for j in range(beg,len(s)):
        if s[j]==i:
            ok=True
            beg=j+1
            break
    if not ok:
        print("NO")
        break
else:
    print("YES")