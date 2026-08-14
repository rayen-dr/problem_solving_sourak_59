''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

import math
t=int(input())
for _ in range(t):
    s=input()
    count_of_zeros=s.count("0")
    count_of_ones=s.count("1")
    operations=min(count_of_ones,count_of_zeros)
    if operations%2!=0:
        print("DA")
    else:
        print("NET")