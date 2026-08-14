''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if len(Counter(a))>=3:
        print("NO")
    else:
        if next(iter(Counter(a).values()))==list(Counter(a).values())[-1]:
            print("YES")
        elif n%2==1 and abs(next(iter(Counter(a).values()))-list(Counter(a).values())[-1])==1:
            print("YES")
        else:
            print("NO")