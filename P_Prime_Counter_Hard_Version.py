import math
#Sieve of Eratosthenes:
limit=(10**6)+1
primy=[True]*limit
primy[0]=primy[1]=False
for i in range(2,math.isqrt(limit-1)+1):
    if primy[i]:
        for j in range(i*i,limit,i):
            primy[j]=False
#--------------------------------------------
n=int(input())
a=list(map(int,input().split()))
print(sum(1 for i in a if primy[i]))
