'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
from collections import Counter
n=int(input())
a=list(map(int,input().split()))
p=list(map(int,input().split()))
levels=set()
for i in range(1,a[0]+1):
    levels.add(a[i])
for i in range(1,p[0]+1):
    levels.add(p[i])
if len(levels)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")