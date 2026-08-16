t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    case1=""
    for i in range(n):
        if i%2==0:
            case1+="a"
        else:
            case1+="b"
    case2=""
    for i in range(n):
        if i%2==1:
            case2+="a"
        else:
            case2+="b"
    def check(case0):
        miss=[i for i in range(n) if s[i]!=case0[i]]
        if not miss:
            return True
        if miss !=list(range(miss[0],miss[-1]+1)):
            return False
        l,r=miss[0],miss[-1]
        sub=s[l:r+1]
        if s[:l]+sub[::-1]+s[r+1:]==case0:
            return True
        flip=''.join('a' if ch=='b' else 'b' for ch in sub)
        if s[:l]+flip+s[r+1:]==case0:
            return True
        elif s[:l]+flip[::-1]+s[r+1:]==case0:
            return True
        return False
    ok=check(case1)or check(case2)
    print("YES" if ok else "NO")