t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    odd=sum(1 for num in a if num%2==1)
    even=n-odd
    flag=False
    for i in range(1,odd+1,2):
        if i<=x and (x-i)<=even:
            flag=True
            break
    print("Yes" if flag else "No")