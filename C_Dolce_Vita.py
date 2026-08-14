def p_sum(p):
    n=len(p)
    p1=[0]*n
    p1[0]=a[0]
    for i in range(1,n):
        p1[i]=p1[i-1]+p[i]
    return p1

def pf(val,ind,x,mid):
    return val+(1*(ind+1)*(mid-1))<=x

def binarySEARCH(val,ind,x):
    l,r=1,1000000005
    res=0
    while l<=r:
        mid=(l+r)//2
        if pf(val,ind,x,mid):
            res=mid
            l=mid+1
        else:
            r=mid-1
    return res

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    p=p_sum(a)
    res=0
    for i in range(n):
        res+=binarySEARCH(p[i],i,x)
    print(res)