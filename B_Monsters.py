t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    l=[]
    for i in range(n):
        l.append((a[i],i+1))
    for i in range(n):
        l[i]=(l[i][0]%k,l[i][1])
        if l[i][0]==0:
            l[i]=(k,l[i][1])
    l.sort(key=lambda a: (-a[0],a[1]))
    res=' '.join(str(hp[1]) for hp in l)
    print(res)