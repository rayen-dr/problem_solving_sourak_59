'''
 ▄▄▄▄▄     ▄▄    ▄▄  ▄▄    ▄▄  ▄▄                    ▄▄▄▄       ▄▄     ▄▄▄▄▄▄    ▄▄▄   ▄▄     ▄▄    ▄▄▄    ▄▄▄ ▄▄▄   ▄▄ 
 ██▀▀▀██   ██    ██  ██    ██  ██                   ██▀▀██     ████    ██▀▀▀▀██  ███   ██    ████    ██▄  ▄██  ███   ██ 
 ██    ██  ██    ██  ██    ██  ██                  ██    ██    ████    ██    ██  ██▀█  ██    ████     ██▄▄██   ██▀█  ██ 
 ██    ██  ████████  ██    ██  ██                  ██    ██   ██  ██   ███████   ██ ██ ██   ██  ██     ▀██▀    ██ ██ ██ 
 ██    ██  ██    ██  ██    ██  ██         █████    ██    ██   ██████   ██  ▀██▄  ██  █▄██   ██████      ██     ██  █▄██ 
 ██▄▄▄██   ██    ██  ▀██▄▄██▀  ██▄▄▄▄▄▄             ██▄▄██▀  ▄██  ██▄  ██    ██  ██   ███  ▄██  ██▄     ██     ██   ███ 
 ▀▀▀▀▀     ▀▀    ▀▀    ▀▀▀▀    ▀▀▀▀▀▀▀▀              ▀▀▀██   ▀▀    ▀▀  ▀▀    ▀▀▀ ▀▀   ▀▀▀  ▀▀    ▀▀     ▀▀     ▀▀   ▀▀▀ 
'''  
primes=[]
for i in range(2,100001):
    is_prime=True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        primes.append(i)
        
t=int(input())
for _ in range(t):
    d=int(input())
    p=-1
    for prime in primes:
        if prime>=(1+d):
            p=prime
            break
    q=-1
    for prime in primes:
        if prime >=(p+d):
            q=prime
            break
    a=min(p*p*p,p*q)
    print(a)
    