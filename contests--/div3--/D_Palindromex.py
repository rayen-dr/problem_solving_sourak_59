t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    first=[-1]*n
    second=[-1]*n
    mex1=0
    for i in range(2*n):
        if first[a[i]]==-1:
            first[a[i]]=i
        else:
            second[a[i]]=i
    left=min(first[0],second[0])
    right=max(first[0],second[0])
    if (right-left+1)%2==0:
        mex1=1
        for i in range(1,n):
            l=first[i]
            r=second[i]
            if l<left and r>right and (r-l+1)%2==0:
                left,right=l,r
                mex1=i+1
            elif l<=right and r>=left and (max(right,r)-min(left,l)+1)%2==0:
                left=min(left,l)
                right=max(right,r)
                mex1=i+1
            else:
                break

    mex2=1
    left,right=first[0],first[0]
    for i in range(1,n):
        l=first[i]
        r=second[i]
        if l==left+1 and r==right+1:
            left,right=l,r
            mex2=i+1
        else:
            break
    mex3=1
    left,right=second[0],second[0]
    for i in range(1,n):
        l=first[i]
        r=second[i]
        if l==left+1 and r==right+1:
            left,right=l,r
            mex3=i+1
        else:
            break
    mex4=0
    if a==a[::-1]:
        mex4=n
    print(max(mex1,mex2,mex3,mex4))
    