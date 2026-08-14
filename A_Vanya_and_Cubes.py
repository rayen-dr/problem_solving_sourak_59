n=int(input())
height=0
used=0
i=1
while True:
    need=i*(i+1)//2
    if used+need>n:
        break
    used+=need
    height+=1
    i+=1
print(height)
