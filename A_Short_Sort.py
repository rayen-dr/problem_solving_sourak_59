t=int(input())
for _ in range(t):
    s=input()
    s_verif="abc"
    res=2
    for i in range(len(s)):
        if s_verif[i]!=s[i]:
            res-=1
    print("YES" if res>=0 else "NO")