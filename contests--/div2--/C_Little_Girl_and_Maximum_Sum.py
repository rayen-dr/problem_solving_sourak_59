def pref(p):
    n=len(p)
    p1=[0]*(n+1)
    for i in range(1,n+1):
        p1[i]=p1[i-1]+p[i-1]
    return p1
n,q=map(int,input().split())
a=list(map(int,input().split()))
diff=[0]*(n+1)
for _ in range(q):
    l,r=map(int,input().split())
    diff[l]+=1
    if  r+1<=n: diff[r+1]-=1
freq=pref(diff)
a.sort(reverse=True)
freq.sort(reverse=True)
sum_res=sum(a*f for a,f in zip(a,freq))
print(sum_res)
    