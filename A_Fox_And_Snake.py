'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
     
n,m=map(int,input().split())
ch="#"*m
ch1="."*(m-1)+"#"
ch2="#"+"."*(m-1)
next=True
for i in range(n):
    if i%2==0:
        print(ch)
    else:
        if next:
            print(ch1)
            next=not(next)
        else:
            print(ch2)
            next=not(next)
