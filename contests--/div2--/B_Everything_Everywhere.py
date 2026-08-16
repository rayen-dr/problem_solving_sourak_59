import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    county=0
    for i in range(n-1):
        if abs(a[i]-a[i+1])==math.gcd(a[i],a[i+1]):
            county+=1
    print(county)