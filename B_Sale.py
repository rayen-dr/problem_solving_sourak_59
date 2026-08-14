def max_sum(a,k):
    negatives=[ x for x in a if x<0]
    negatives_sort=sorted(negatives,key=lambda x: abs(x),reverse=True)
    return sum(abs(x) for x in negatives_sort[:k])
n,m=map(int,input().split())
a=list(map(int,input().split()))
print(max_sum(a,m))
        