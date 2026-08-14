'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input().strip()
    
    #prefix_sum-------------------------------------
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1]=prefix[i]+(1 if s[i]=="W" else 0)
    #------------------------------------------------
    
    minimun_cells=float('inf')
    for i in range(n-k+1):
        
        #sliding window-----------
        diff=prefix[i+k]-prefix[i]
        #-------------------------
        
        minimun_cells=min(minimun_cells,diff)
    
    print(minimun_cells)