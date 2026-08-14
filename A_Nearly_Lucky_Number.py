''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
from collections import Counter
n=input().strip()
new_n=n.count('7')+n.count('4')
n_dict=Counter(str(new_n))
failed=False
for key in n_dict.keys():
    if key not in ['7','4']:
        print("NO")
        failed=True
        break
if not failed:
    print("YES")