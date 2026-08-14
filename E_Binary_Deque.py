t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    v=list(map(int,input().split()))
    leni=-1
    mp = {0: -1}
    sum = 0
    for i in range(n):
        sum += v[i]
        if sum - s in mp:
            leni = max(leni, i - mp[sum - s])
        if sum not in mp:
            mp[sum] = i
    if leni == -1:
        print("-1")
    else:
    	print(n - leni)