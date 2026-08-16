t=int(input())
for _ in range(t):
    p,q=map(int,input().split())
    if (3*p)%(2*q)<=min(p,q)-1:
        print("Bob")
    else:
        print("Alice")