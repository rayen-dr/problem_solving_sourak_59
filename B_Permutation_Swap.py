'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
import math
t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    k=abs(p[0]-1)
    for i in range(1,n):
        k=math.gcd(k,abs(p[i]-(i+1)))
    print(k)