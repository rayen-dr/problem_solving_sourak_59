t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    buffer=[]
    elem_2=[]
    elem_3=[]
    elem_6=[]
    for i in a:
        if i%2==0 and i%3!=0:
            elem_2.append(i)
        elif i%2==1 and i%3==0:
            elem_3.append(i)
        elif i%6==0:
            elem_6.append(i)
        else:
            buffer.append(i)
    res=elem_2+buffer+elem_3+elem_6
    print(*res)
    
    