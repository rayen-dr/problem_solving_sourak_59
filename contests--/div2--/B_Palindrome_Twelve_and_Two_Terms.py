import sys
input=sys.stdin.readline
def solve(n):
    s=str(n)
    d=len(s)    
    def make_palindrome(p_str,length):
        odd=(length%2==1)
        if odd:
            return int(p_str+p_str[-2::-1])
        else:
            return int(p_str+p_str[::-1])
    for length in range(d,0,-1):
        half=(length+1)//2
        if length==d:
            prefix_num=int(s[:half])
        else:
            prefix_num=int('9'*half)
        
        for delta in range(14):
            p=prefix_num-delta
            if p<=0:
                if length==1:
                    a,b=0,n
                    if b%12==0:
                        return a,b
                break
            a=make_palindrome(str(p),length)
            if a<=n:
                b=n-a
                if b%12==0:
                    return a,b
    return None
t=int(input())
out=[]
for _ in range(t):
    n=int(input())
    res=solve(n)
    out.append(f'{res[0]} {res[1]}' if res else '-1')
print('\n'.join(out))
