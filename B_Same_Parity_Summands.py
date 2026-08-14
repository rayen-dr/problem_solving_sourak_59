t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if n>=k and (n-k)%2==0:
        print("YES")
        res=[1]*(k-1)+[n-(k-1)]
        print(*res)
    elif n>=2*k and (n%2==0):
        print("YES")
        res=[2]*(k-1)+[n-2 *(k-1)]
        print(*res)
    else:
        print("NO")
    