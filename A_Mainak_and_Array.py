'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    answer=a[n-1]-a[0]
    for i in range(1,n):
        answer=max(answer,a[i]-a[0])
    for i in range(n-1):
        answer=max(answer,a[n-1]-a[i])
    for i in range(n-1):
        answer=max(answer,a[i]-a[i+1])
    print(answer)