t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    L=0
    for i in range(n-1):
        if a[i]>a[i+1]:
            L=max(L,a[i]-a[i+1])
    can0=True
    can1=True
    for i in range(n-1):
        ncan0=False
        ncan1=False
        for x,okx in [(0,can0),(1,can1)]:
            if not okx:
                continue
            for y in [0,1]:
                ok=False
                if a[i]>a[i+1]:
                    if x==0 and y==1:
                        ok=True
                elif a[i]==a[i+1]:
                    if not(x==1 and y==0):
                        ok=True
                else:
                    d=a[i+1]-a[i]
                    if x==1 and y==0:
                        if d>=L:
                            ok=True
                    else:
                        ok=True
                if ok:
                    if y==0:
                        ncan0=True
                    else:
                        ncan1=True
        can0=ncan0
        can1=ncan1
    print("YES" if can0 or can1 else "NO")