''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    final_pos=0
    if n%4==1:
        final_pos=-n
    elif n%4==2:
        final_pos=1
    elif n%4==3:
        final_pos=n+1
    else:
        final_pos=0
    if x%2==0:
        final_pos+=x
    else:
        final_pos=x-final_pos
    print(final_pos)  