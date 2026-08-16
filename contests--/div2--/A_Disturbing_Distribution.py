t=int(input())
mod=676767677
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))==1 and a[0]==1:
        print(1)
    else:
        res=0
        for i in a:
            if i!=1:
                res+=i
        if a[-1]==1:
            res+=1
        print(res%mod)