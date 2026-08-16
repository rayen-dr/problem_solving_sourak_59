import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs_iter(i, j):
    stack = [(i, j, -1, -1)]
    while stack:
        x, y, px, py = stack.pop()
        if vis[x][y]:
            continue
        vis[x][y] = True
        for c in range(4):
            di, dj = x + dx[c], y + dy[c]
            if di < 0 or di >= n or dj < 0 or dj >= m:
                continue
            if tab[di][dj] != tab[x][y]:
                continue
            if vis[di][dj] and (di, dj) != (px, py):
                return True
            if not vis[di][dj]:
                stack.append((di, dj, x, y))
    return False

def isCycle():
    for i in range(n):
        for j in range(m):
            if not vis[i][j]:
                if dfs_iter(i, j):
                    return True
    return False

n, m = map(int, input().split())
tab = [list(input().strip()) for _ in range(n)]
vis = [[False] * m for _ in range(n)]

for i in range(n - 1):
    for j in range(m - 1):
        if tab[i][j] == tab[i+1][j] == tab[i][j+1] == tab[i+1][j+1]:
            print("Yes")
            sys.exit()
print("Yes" if isCycle() else "No")