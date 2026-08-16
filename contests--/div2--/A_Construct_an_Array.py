t=int(input())
for _ in range(t):
    n=int(input())
    res=[2*i-1 for i in range(1,n+1)]
    print(*res)
