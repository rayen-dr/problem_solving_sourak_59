'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
n,m=map(int,input().split())
if n==m:
    print(0)
elif n>m:
    print(n-m)
else:
    steps=0
    while m>n:
        if m%2==0:
            m//=2
        else:
            m+=1
        steps+=1
    print(steps+(n-m))
#there is a BFS approach early to work with but it's undrestandable !
