t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if (x%2==0 and y%2==0)or((x%2==1 and y%2==0)or(x%2==0 and y%2==1)):
        print("YES")
    else:
        print("NO")