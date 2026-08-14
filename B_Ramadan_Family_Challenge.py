'''Ramadan Mubarak, 
May your code be accepted like your prayers'''
n=int(input())
if n%2==0:
    k=n//2
    print(k)
    print("2 "*k)
else:
    k=(n-1)//2
    print(k)
    print("2 "*(k-1)+"3")
