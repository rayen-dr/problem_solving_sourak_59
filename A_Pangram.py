'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
from collections import Counter
n=int(input())
s=input()
alphabet="azertyuiopmlkjhgfdsqwxcvbn"
s_dict=Counter(s.lower())
done=True
for i in alphabet:
    if i not in s_dict:
        done=False
        print("NO")
        break
if done:
    print("YES")