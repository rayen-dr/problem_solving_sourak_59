t=int(input())
for _ in range(t):
    s=input()
    for i in range(len(s)):
        if s[:i]==s[i:]:
            print("YES")
            break
    else:
        print("NO")
