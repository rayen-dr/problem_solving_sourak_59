t=int(input())
for _ in range(t):
    n,c=map(str,input().split())
    n=int(n)
    s=input()
    if len(set(s))==1 and s[0]==c:
        print(0)
        continue
    if s[-1]==c:
        print(1)
        print(n)
        continue
    val=-1
    for i in range(2,n+1):
        check=True
        for j in range(i,n+1,i):
            if s[j-1]!=c:
                check=False
                break
        if check:
            val=i
            break
    if val!=-1:
        print("1")
        print(val)
        continue
    print("2")
    print(n-1,n)