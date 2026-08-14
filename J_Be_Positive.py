t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c1=a.count(-1)
    c0=a.count(0)
    c1=(c1%2)*2
    print(c0+c1)