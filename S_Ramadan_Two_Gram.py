from collections import Counter
n=int(input())
s=input().strip()
d=[]
for i in range(n-1):
    d.append(s[i:i+2])
print((Counter(d)).most_common(1)[0][0])