n=int(input())
a=list(map(int,input().split()))
if a==sorted(a):
    print("yes")
    print(1,1)
else:
    l=0
    for i in range(1,n):
        if a[i]<a[i-1]:
            l=i-1
            break
    r=n-1
    for i in range(n-1,0,-1):
        if a[i]<a[i-1]:
            r=i
            break
    b=a[:l]+(a[l:r+1])[::-1]+a[r+1:]
    if b==sorted(a):
        print("yes")
        print(l+1,r+1)
    else:
        print("no")


        