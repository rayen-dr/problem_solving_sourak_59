''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=float('inf')
    even_count=0
    for num in a:
        if num%2==0:
            even_count+=1
        if num%k==0:
            ans=0
        ans=min(ans,(k-num%k))
    if k==4:
        if even_count>=2:
            ans=min(ans,0)
        elif even_count==1:
            ans=min(ans,1)
        elif even_count==0:
            ans=min(ans,2)
    print(ans)