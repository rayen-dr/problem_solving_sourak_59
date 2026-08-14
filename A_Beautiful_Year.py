''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

def distinct_digit_years():
    years_under_fingertips=[]
    for y in range(1000,10000):
        ch=str(y)
        if len(set(ch))==4:
            years_under_fingertips.append(y)
    return years_under_fingertips

n=int(input())
years=distinct_digit_years()
for _ in years:
    if n<_:
        print(_)
        break
    
