t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    a.sort()
    print(max(a)*2-sum(a))