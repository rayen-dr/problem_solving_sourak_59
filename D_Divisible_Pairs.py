'''from collections import Counter
import math
t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    res=0
    reste_x=[]
    reste_y=[]
    for i in a:
        reste_x.append(i%x)
        reste_y.append(i%y)
    res
    '''
from collections import Counter
t=int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    res=0
    cnt=Counter()
    for i in a:
        rx,ry=i%x,i%y
        res+=cnt[((x-rx)%x,ry)]
        cnt[(rx,ry)]+=1
    print(res)

    