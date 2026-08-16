''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n,h,l=map(int,input().split())
    a=list(map(int,input().split()))
    count_fitted_rows,count_fitted_columns,count_fitted_both=0,0,0
    for i in a:
        if i<=h and i<=l:
            count_fitted_both+=1
        elif i<=h:
            count_fitted_rows+=1
        elif i<=l:
            count_fitted_columns+=1
    res=min(count_fitted_rows,count_fitted_columns)
    contrainte1=(count_fitted_rows+count_fitted_columns)-(2*res)
    res+=min(contrainte1,count_fitted_both)+(count_fitted_both-min(contrainte1,count_fitted_both))//2
    print(res)