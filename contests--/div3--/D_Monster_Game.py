''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

import bisect

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    p=[0]*(n+1)
    for i in range(1,n+1):
        p[i]=p[i-1]+b[i-1]
    a.sort()
    max_score=0
    for i in range(n):
        x=a[i]
        cnt=n-i
        k=bisect.bisect(p,cnt)-1
        max_score=max(max_score,x*k)
    print(max_score)