''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

s=input().strip()
count_uppercases=0
count_lowercases=0
for i in s:
    if ord('A')<=ord(i)<=ord('Z'):
        count_uppercases+=1
    else:
        count_lowercases+=1
if count_lowercases>=count_uppercases:
    print(s.lower())
else:
    print(s.upper())