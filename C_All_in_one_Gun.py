import sys; 
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
input=sys.stdin.readline
for i in range(int(input())):
    n,h,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    if h%s==0:
        print(((h//s)-1)*k+n*(h//s))
    else:
        d=h//s
        ans=d*k+n*d
        l,r=1,n-1
        res=n
        x=h%s
        while l<=r:
            mid=(l+r)//2
            cur,mino=sum(a[:mid]),min(a[:mid])
            maxo=max(a[mid:])
            if cur+int(maxo>mino)*(maxo-mino)>=x:
                res=mid
                r=mid-1
            else:
                l=mid+1
        print(ans+res)