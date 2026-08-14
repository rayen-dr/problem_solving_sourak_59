t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    count_0s=s.count("0")
    if count_0s%2==0:
        print("BOB")
    else:
        if count_0s==1:
            print("BOB")
            continue
        print("ALICE")