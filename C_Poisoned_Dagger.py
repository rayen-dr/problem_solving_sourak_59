t=int(input())
for _ in range(t):
    n,h=map(int,input().split())
    a=list(map(int,input().split()))
    
    def damage(k):
        total=0
        for i in range(n-1):
            total+=min(k,a[i+1]-a[i])
        total+=k
        return total
    l,r=1,h
    while l<r:
        mid=(l+r)//2
        if damage(mid)>=h:
            r=mid
        else:
            l=mid+1
    print(l)