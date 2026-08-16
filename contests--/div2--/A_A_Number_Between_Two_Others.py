t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    k=y//x
    print("YES" if k>2 else "NO")