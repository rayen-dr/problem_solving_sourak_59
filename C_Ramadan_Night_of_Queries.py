'''Ramadan Mubarak, 
May your code be accepted like your prayers'''
def p_sum(p):
    n=len(p)
    p1=[0]*(n+1)
    for i in range(1,n+1):
        p1[i]=p1[i-1]+p[i-1]
    return p1
t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        a[i]=max(a[i],b[i])
    for i in range(n-2,-1,-1):
        a[i]=max(a[i],a[i+1])
    p=p_sum(a)
    res=[]
    for query in range(q):
        l,r=map(int,input().split())
        res.append(p[r]-p[l-1])
    print(*res)