''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    v=[]
    for i in range(n):
        v.append((b[i],a[i]))
    v.sort()
    mcost=p
    shared=1
    for i,j in v:
        if i>=p:
            break 
        if shared+j>n:
            mcost+=(n-shared)*i 
            shared=n 
        else:
            mcost+=j*i 
            shared+=j 
    mcost+=(n-shared)*p 
    print(mcost)