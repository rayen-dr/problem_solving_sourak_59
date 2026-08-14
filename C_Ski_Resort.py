t=int(input())
for _ in range(t):
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    afirst=[]
    for i in range(n):
        if a[i]<=q:
            afirst.append(1)
        else:
            afirst.append(0)
    ways=0
    c1s=0
    for i in range(n):
        if afirst[i]==1:
            c1s+=1
        else:
            if c1s>=k:
                diff=c1s-k+1
                ways+=(diff*(diff+1)//2)
            c1s=0
    if c1s>=k:
        diff=c1s-k+1
        ways+=(diff*(diff+1)//2)
    print(ways)