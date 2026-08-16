from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    s=input().strip()
    d=Counter(s)
    if ')' in d and '(' in d:
        if d['(']==d[')']:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
                