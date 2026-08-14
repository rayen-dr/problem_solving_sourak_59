'''
 ▄▄▄▄▄     ▄▄    ▄▄  ▄▄    ▄▄  ▄▄                    ▄▄▄▄       ▄▄     ▄▄▄▄▄▄    ▄▄▄   ▄▄     ▄▄    ▄▄▄    ▄▄▄ ▄▄▄   ▄▄ 
 ██▀▀▀██   ██    ██  ██    ██  ██                   ██▀▀██     ████    ██▀▀▀▀██  ███   ██    ████    ██▄  ▄██  ███   ██ 
 ██    ██  ██    ██  ██    ██  ██                  ██    ██    ████    ██    ██  ██▀█  ██    ████     ██▄▄██   ██▀█  ██ 
 ██    ██  ████████  ██    ██  ██                  ██    ██   ██  ██   ███████   ██ ██ ██   ██  ██     ▀██▀    ██ ██ ██ 
 ██    ██  ██    ██  ██    ██  ██         █████    ██    ██   ██████   ██  ▀██▄  ██  █▄██   ██████      ██     ██  █▄██ 
 ██▄▄▄██   ██    ██  ▀██▄▄██▀  ██▄▄▄▄▄▄             ██▄▄██▀  ▄██  ██▄  ██    ██  ██   ███  ▄██  ██▄     ██     ██   ███ 
 ▀▀▀▀▀     ▀▀    ▀▀    ▀▀▀▀    ▀▀▀▀▀▀▀▀              ▀▀▀██   ▀▀    ▀▀  ▀▀    ▀▀▀ ▀▀   ▀▀▀  ▀▀    ▀▀     ▀▀     ▀▀   ▀▀▀ 
'''  
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    arr=[]
    for i in range(1,n+1):
        arr.append((a[i-1],i))
    arr.sort(key=lambda x:x[0])
    nxt=[0]*(n+1)
    sum_prefix=[0]*(n+1)
    res=[0]*(n+1)
    nxt[0]=0
    sum_prefix[0]=0
    for i in range(1,n+1):
        if nxt[i-1]>=i:
            nxt[i]=nxt[i-1]
            sum_prefix[i]=sum_prefix[i-1]
        else:
            sum_prefix[i]=sum_prefix[i-1]+arr[i-1][0]
            nxt[i]=i
            while nxt[i]<n and sum_prefix[i]>=arr[nxt[i]][0]:
                nxt[i]+=1
                sum_prefix[i]+=arr[nxt[i]-1][0]
        res[arr[i-1][1]]=nxt[i]
    print(" ".join(str(res[i]-1) for i in range(1,n+1)))