t=int(input())
for _ in range(t):
    n=int(input())
    if (n//2)%2==1:
        print("NO")
    else:
        print("YES")
        n//=2
        evens=[2*i for i in range(1,n+1)]
        odds=[2*i-1 for i in range(1,n)]+[3*n-1]
        print(*evens,*odds)