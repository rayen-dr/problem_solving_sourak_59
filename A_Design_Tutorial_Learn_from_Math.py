def sieve(n):
    prime = [True]*(n+1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return [i for i, val in enumerate(prime) if val]

n=int(input())
if n%4==0:
    print(n//2,n//2)
else:
    s=set(sieve(n))
    for k in range(2,n+1):
        if k not in s and (n-k) not in s :
            print(k,n-k)
            break
    