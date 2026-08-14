''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(map(int,input().split()))
    max_count=1
    count=1
    for i in range(1,n):
        if a[i]==a[i-1]:
            count+=1
        else:
            if count>max_count:
                max_count=count
            count=1
    if count>max_count:
        max_count=count
    op=0
    while max_count<n:
        op+=1
        if max_count*2<=n:
            op+=max_count
            max_count*=2
        else:
            op+=(n-max_count)
            max_count=n
    print(op)        