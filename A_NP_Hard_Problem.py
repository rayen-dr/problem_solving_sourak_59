n,m=map(int,input().split())
fl=False
f=[0]*100001
E=[[] for i in range(n+1)]
e=[tuple(map(int,input().split())) for _ in range(m)]

for u,v in sorted(e):
    E[u]+=[v];E[v]+=[u]

def bfs(nom,col):
    ch=[(nom,col)]
    while ch:
        v,c=ch.pop()
        if f[v]==0:
            f[v]=c
            for u in E[v]:
                if f[u]==0:
                    ch+=[(u,3-c)]
for x in range(1,n+1):
    if f[x]==0:bfs(x,1)
for u,v in e:
    if f[u]==f[v]:
        fl=True;
        break
if fl:print(-1)
else:
    a=[i for i in range(n+1)if f[i]==1]
    b=[i for i in range(n+1)if f[i]==2]
    print(len(a));print(*a)
    print(len(b));print(*b)
