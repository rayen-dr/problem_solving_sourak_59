import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    s=input().strip()
    ans=0
    pending=0 
    for c in s:
        if c=='4':
            ans+=1
        elif c=='1' or c=='3':
            pending+=1
        elif c=='2':
            if pending>0:
                ans+=1   
                pending-=1
    print(ans)

