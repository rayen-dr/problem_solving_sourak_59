'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
    
n=int(input())
teams=[]
for _ in range(n):
    h,g=map(int,input().split())
    teams.append((h,g))
ans=0
for i in range(n):
    for j in range(n):
        if i!=j and teams[i][0]==teams[j][1]:
            ans+=1
print(ans)
