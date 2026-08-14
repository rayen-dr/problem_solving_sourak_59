''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    s=input().strip()
    count_of_zeros=s.count("0")
    count_of_ones=s.count("1")
    length_of_t=0
    for char in s:
        if char=='0' and count_of_ones>0:
            count_of_ones-=1
            length_of_t+=1
        elif char=='1' and count_of_zeros>0:
            count_of_zeros-=1
            length_of_t+=1
        else:
            break
    print(len(s)-length_of_t)