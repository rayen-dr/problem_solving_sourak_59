t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    v=[[] for _ in range(m)]
    for j in range(n):
        card_numbers=list(map(int,input().split()))
        for i in range(m):
            v[i].append(card_numbers[i])
    for i in range(m):
        v[i].sort()
    ans=0
    for i in range(m):
        for j in range(n):
            ans-=(v[i][j]*(n-j-1))
            ans+=(v[i][j]*j)
    print(ans)
