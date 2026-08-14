import sys
def can_fill(mid,heights,x):
    units=0
    for h in heights:
        if h<mid:
            units+=(mid-h)
    return units<=x
t=int(sys.stdin.readline().strip())
for _ in range(t):
    n,x=map(int, sys.stdin.readline().split())
    heights=list(map(int, sys.stdin.readline().split()))
    low,high,ans=1,int(1e12),-1
    while low<=high:
        mid=(low+high)//2
        if can_fill(mid,heights,x):
            ans=mid
            low=mid+1  
        else:
            high=mid-1 
    print(ans)
