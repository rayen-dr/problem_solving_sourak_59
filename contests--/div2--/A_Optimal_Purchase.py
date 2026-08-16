t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    if 3*a>b:
        if n%3==0:
            print((n//3)*b)
        else:
            c=(n//3)
            if (n%3)*a>=b:
                print((c+1)*b)
            else:
                print(c*b+(n%3)*a)
    else:
        print(n*a)