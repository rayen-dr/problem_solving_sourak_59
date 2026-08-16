import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    max_p = 0
    max_a = 0
    possible = True
    
    for i in range(n):
        max_p = max(max_p, p[i])
        max_a = max(max_a, a[i])
        if max_a > max_p:
            possible = False
            break
    
    print("YES" if possible else "NO")
