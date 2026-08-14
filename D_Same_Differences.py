'''
 ▄▄▄▄▄     ▄▄    ▄▄  ▄▄    ▄▄  ▄▄                    ▄▄▄▄       ▄▄     ▄▄▄▄▄▄    ▄▄▄   ▄▄     ▄▄    ▄▄▄    ▄▄▄ ▄▄▄   ▄▄ 
 ██▀▀▀██   ██    ██  ██    ██  ██                   ██▀▀██     ████    ██▀▀▀▀██  ███   ██    ████    ██▄  ▄██  ███   ██ 
 ██    ██  ██    ██  ██    ██  ██                  ██    ██    ████    ██    ██  ██▀█  ██    ████     ██▄▄██   ██▀█  ██ 
 ██    ██  ████████  ██    ██  ██                  ██    ██   ██  ██   ███████   ██ ██ ██   ██  ██     ▀██▀    ██ ██ ██ 
 ██    ██  ██    ██  ██    ██  ██         █████    ██    ██   ██████   ██  ▀██▄  ██  █▄██   ██████      ██     ██  █▄██ 
 ██▄▄▄██   ██    ██  ▀██▄▄██▀  ██▄▄▄▄▄▄             ██▄▄██▀  ▄██  ██▄  ██    ██  ██   ███  ▄██  ██▄     ██     ██   ███ 
 ▀▀▀▀▀     ▀▀    ▀▀    ▀▀▀▀    ▀▀▀▀▀▀▀▀              ▀▀▀██   ▀▀    ▀▀  ▀▀    ▀▀▀ ▀▀   ▀▀▀  ▀▀    ▀▀     ▀▀     ▀▀   ▀▀▀ 
'''  
from collections import Counter
import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    diff_a=[]
    for i in range(n):
        diff_a.append(a[i]-(i+1))
    occ_diff_a=Counter(diff_a)
    #debug()
    #print(diff_a)
    #print(occ_diff_a)
    res=0
    for freq in occ_diff_a.values():
        res+=freq*(freq-1)//2
    print(res)