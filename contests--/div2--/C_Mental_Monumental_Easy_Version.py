t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    reachable=[False]*(n)
    for i in range(n):
        if i>a[i] :
            continue
        else: 
            if a[i]-i==1:
                continue
            else:
                reachable[i]=True
    s=set()
    a_set=set()
    for i in range(n):
        if reachable[i]==False:
            s.add(i)
            a_set.add(a[i])
    for i in range(n):
        if reachable[i]==False:
            if i in a_set:
                s.remove(i)
                a_set.remove(a[i])
                reachable[i]=True
    print(n-len(s))
    