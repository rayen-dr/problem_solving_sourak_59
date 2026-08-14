from queue import Queue
n,m=map(int,input().split())
a=list(map(int,input().split()))

q=Queue()
for i in range(n):
    q.put((a[i],i+1))
    

while q.qsize()!=1:
    c=q.get()
    if c[0]-m>0:
        q.put((c[0]-m,c[1])) #c[1]: position  

print(q.get()[1])