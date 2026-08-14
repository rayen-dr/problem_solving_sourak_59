'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
from collections import Counter
n=int(input())
s=list(map(int,input().split()))
dict_s=Counter(s)
count_taxi=dict_s[4]+dict_s[3]
dict_s[1]=max(0,dict_s[1]-dict_s[3])
count_taxi+=dict_s[2]//2
if dict_s[2]%2:
    count_taxi+=1
    dict_s[1]=max(0,dict_s[1]-2)
if dict_s[1]>0:
    count_taxi+=(dict_s[1]+3)//4
print(count_taxi)
