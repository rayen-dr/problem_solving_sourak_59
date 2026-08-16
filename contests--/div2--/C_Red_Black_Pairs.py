t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    t=input()
    way1=sum(0 if s[i]==t[i] else 1 for i in range(n))
    way2=0
    ok=False
    for i in range(0,n,2):
        if i+1<n:
            ok=True
            way2+= 0 if s[i]==s[i+1] else 1
            way2+=0 if t[i]==t[i+1] else 1
    if n%2==1:
        way2+=0 if s[n-2]==s[-1] else 1
        way2+=0 if t[n-2]==t[-1] else 1
        
    print(min(way1,way2) if ok else way1)