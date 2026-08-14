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
    ans_a=1
    ans_b=n-1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            ans_a=n//i
            ans_b=n-ans_a
            break
    print(ans_a,ans_b)