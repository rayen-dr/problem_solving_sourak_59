'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

n=int(input())
a=list(map(int,input().split()))
maxi=max(a)
mini=min(a)
max_index=a.index(maxi)
min_index=n-1-a[::-1].index(mini)
res=max_index+(n-1-n+1+a[::-1].index(mini))
if max_index>min_index:
    res-=1
print(res)