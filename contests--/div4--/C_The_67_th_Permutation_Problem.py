t=int(input())
for _ in range(t):
    n=int(input())
    final_perm=[]
    pointer1,pointer2=1,3*n
    for i in range(n):
        final_perm.append(pointer1)
        final_perm.append(pointer2)
        final_perm.append(pointer2-1)
        pointer1+=1
        pointer2-=2
    print(*final_perm)