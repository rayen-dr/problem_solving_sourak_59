def ramadan23(n,m):
    if n==m:
        return 0
    if (m%n)!=0:
        return -1
    r=m//n
    mo=0
    while r%2==0:
        r//=2
        mo+=1
    while r%3==0:
        r//=3
        mo+=1
    if r!=1:
        return -1
    return mo
n,m=map(int,input().split())
print(ramadan23(n,m))