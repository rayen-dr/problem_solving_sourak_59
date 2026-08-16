import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    H = h + h  # doubled for circular indexing

    # pfx[l][k] = max(H[l], H[l+1], ..., H[l+k-1])
    # = max barrier on the clockwise path of length k starting at l
    pfx = [[0] * n for _ in range(n)]
    for l in range(n):
        cur = 0
        for k in range(1, n):
            cur = max(cur, H[l + k - 1])
            pfx[l][k] = cur

    # For vessel l empty, vessel i at clockwise distance k=(i-l)%n holds:
    #   min(R, L) where
    #   R = pfx[l][k]          = max barrier on clockwise path l -> i (length k)
    #   L = pfx[(l+k)%n][n-k]  = max barrier on clockwise path i -> l (length n-k)
    ans = []
    for l in range(n):
        total = 0
        for k in range(1, n):
            R = pfx[l][k]
            L = pfx[(l + k) % n][n - k]
            total += min(R, L)
        ans.append(total)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')

t = int(input())
for _ in range(t):
    solve()