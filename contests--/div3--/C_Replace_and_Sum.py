''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

def prefix_sum(a):
    n=len(a)
    p=[0]*(n+1)
    for i in range(1,n+1):
        p[i]=p[i-1]+a[i-1]
    return p
def range_sum(p,l,r):
    return p[r]-p[l-1]

t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[max(a[-1],b[-1])]
    for i in range(n-1,-1,-1):
        c.append(max(a[i],b[i],c[n-i]))
    p=prefix_sum(c)
    res=[]
    for query in range(q):
        l,r=map(int,input().split())
        res.append(range_sum(p,l,r))
    print(*res)