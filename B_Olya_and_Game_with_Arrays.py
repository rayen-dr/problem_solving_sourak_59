t=int(input())
for _ in range(t):
    n=int(input())
    elem=[]
    MIN=float('inf')
    for _ in range(n):
        m=int(input())
        a=list(map(int,input().split()))
        a.sort()
        elem.append(a[1])
        MIN=min(MIN,a[0])
    elem.sort()
    selem=sum(elem)
    MIN1=elem[0]
    print(MIN+selem-MIN1)