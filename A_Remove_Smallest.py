t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    gaps=[]
    for i in range(n-1):
        gaps.append(a[i+1]-a[i])
    gaps.append(a[n-2]-a[-1])
    ok=True
    for i in gaps:
        if i>1:
            ok=False
            break
    print("YES" if ok else "NO")
    