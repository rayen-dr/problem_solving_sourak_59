                                                                                                                                                                                                                                                                           

def solve():
    s = input()
    if len(s) == 1 or s[1:].isupper():
        s = ''.join([c.lower() if c.isupper() else c.upper() for c in s])
    print(s)

def main():
    t=1
    #t=int(input())
    for _ in range(t):
        solve()

if __name__=="__main__":
    main()