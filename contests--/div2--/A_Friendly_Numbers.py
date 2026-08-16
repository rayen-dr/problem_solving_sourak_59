def d(n):
    return sum(int(c) for c in str(n))
t=int(input())
for _ in range(t):
    x=int(input())
    county=0
    for y in range(x,x+100):
        if y-d(y)==x:
            county+=1
    print(county)