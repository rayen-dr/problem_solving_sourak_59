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
input = sys.stdin.readline

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, delta=1):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

def solve():
    n = int(input())
    a, b = [], []
    distincts = set()
    v = []

    for i in range(n):
        ai, bi, ai2, bi2 = map(int, input().split())
        # correspond au double input du code C++
        a.append(ai)
        b.append(bi)
        distincts.add(bi)
        v.append((ai, -(i+1)))

    q = int(input())
    x, y = [], []
    for i in range(q):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
        distincts.add(yi)
        v.append((xi, i+1))

    # compression des coordonnées
    code = {}
    m = 1
    for val in sorted(distincts):
        code[val] = m
        m += 1

    # tri des événements
    v.sort()

    bit = Fenwick(m)
    ans = [0] * q

    for val, p in v:
        if p < 0:
            idx = -p - 1
            bit.update(code[b[idx]])
        else:
            idx = p - 1
            ans[idx] = bit.query(code[y[idx]])

    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    solve()
