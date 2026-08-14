from math import isqrt
def prime(n):
    for i in range(2,isqrt(n)+1):
        if n%i==0:
            return False
    return True
n=int(input())
a=list(map(int,input().split()))
nb=0
for i in a:
    if prime(i) and i!=1:
        nb+=1
print(nb)
