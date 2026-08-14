'''
 ▄▄▄▄▄     ▄▄    ▄▄  ▄▄    ▄▄  ▄▄                    ▄▄▄▄       ▄▄     ▄▄▄▄▄▄    ▄▄▄   ▄▄     ▄▄    ▄▄▄    ▄▄▄ ▄▄▄   ▄▄ 
 ██▀▀▀██   ██    ██  ██    ██  ██                   ██▀▀██     ████    ██▀▀▀▀██  ███   ██    ████    ██▄  ▄██  ███   ██ 
 ██    ██  ██    ██  ██    ██  ██                  ██    ██    ████    ██    ██  ██▀█  ██    ████     ██▄▄██   ██▀█  ██ 
 ██    ██  ████████  ██    ██  ██                  ██    ██   ██  ██   ███████   ██ ██ ██   ██  ██     ▀██▀    ██ ██ ██ 
 ██    ██  ██    ██  ██    ██  ██         █████    ██    ██   ██████   ██  ▀██▄  ██  █▄██   ██████      ██     ██  █▄██ 
 ██▄▄▄██   ██    ██  ▀██▄▄██▀  ██▄▄▄▄▄▄             ██▄▄██▀  ▄██  ██▄  ██    ██  ██   ███  ▄██  ██▄     ██     ██   ███ 
 ▀▀▀▀▀     ▀▀    ▀▀    ▀▀▀▀    ▀▀▀▀▀▀▀▀              ▀▀▀██   ▀▀    ▀▀  ▀▀    ▀▀▀ ▀▀   ▀▀▀  ▀▀    ▀▀     ▀▀     ▀▀   ▀▀▀ 
'''  
#Mtaylor solution;
import sys
from collections import defaultdict

def solve():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)

    # Prétraitement plus léger
    freq = defaultdict(int)
    stack = [(0, n-1, 0)]
    while stack:
        l, r, lstmn = stack.pop()
        if l > r:
            continue
        mn = min(a[l:r+1])  # direct min, pas de segment tree
        freq[r-l+1] += mn - lstmn
        # Découpage par positions du minimum
        for i in range(l, r+1):
            if a[i] == mn:
                stack.append((l, i-1, mn))
                l = i+1
        stack.append((l, r, mn))

    cur = n
    for _ in range(q):
        k = int(input())
        while cur >= 1 and k:
            m = min(freq[cur], k)
            k -= m
            freq[cur] -= m
            total -= m * cur
            if freq[cur] == 0:
                cur -= 1
        print(total)

if __name__ == "__main__":
    solve()
