t=int(input())
for _ in range(t):
    s=input().strip()
    ch="codeforces"
    res=0
    for i in range(10):
        if ch[i]!=s[i]:
            res+=1
    print(res)