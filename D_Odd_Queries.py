'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    old_sum=sum(a)
    
    #prefix_sum**---------------------------
    prefix_sum=[0]*(n+1)
    for i in range(1,n+1):
        prefix_sum[i]=prefix_sum[i-1]+a[i-1]
    #---------------------------------------
    
    for _ in range(q):
        l,r,k=map(int,input().split())
        sum_to_remove=prefix_sum[r]-prefix_sum[l-1]
        sum_to_add=(r-l+1)*k
        total_sum=old_sum-sum_to_remove+sum_to_add
        if total_sum%2==1:
            print("YES")
        else:
            print("NO")    