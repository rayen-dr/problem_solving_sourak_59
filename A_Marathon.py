t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    res=0
    for j in l:
        if j>l[0]:
            res+=1
    print(res)