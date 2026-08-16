t=int(input())
for _ in range(t):
    n=int(input())
    c=list(map(int, input().split()))
    c.sort()
    total_A=sum(x for x in c if x>=2)
    ans_A=total_A if total_A>=3 else 0
    max_c=c[-1]
    m=min(n-1,max_c // 2)
    total_B=max_c+sum(c[-(m+1):-1])
    ans_B=total_B if total_B>=3 else 0
    print(max(ans_A,ans_B))

# haya 3aaad foookk 