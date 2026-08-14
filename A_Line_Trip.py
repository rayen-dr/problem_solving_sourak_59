''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
    
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a=[0]+a
    a.append(x)
    n=len(a)
    max_distance_between_pts=-float('inf')
    for i in range(1,n):
        if i==n-1:
            max_distance_between_pts=max(max_distance_between_pts,2*(a[i]-a[i-1]))
        else:
            max_distance_between_pts=max(max_distance_between_pts,a[i]-a[i-1])
    print(max_distance_between_pts)