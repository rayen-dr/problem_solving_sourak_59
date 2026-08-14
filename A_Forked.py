''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
dx=[-1,1,-1,1]
dy=[-1,-1,1,1]
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    xk,yk=map(int,input().split())
    xq,yq=map(int,input().split())
    king_hits=set()
    queen_hits=set()
    for j in range(4):
        king_hits.add((xk+dx[j]*a,yk+dy[j]*b))
        king_hits.add((xk+dx[j]*b,yk+dy[j]*a))
        queen_hits.add((xq+dx[j]*a,yq+dy[j]*b))
        queen_hits.add((xq+dx[j]*b,yq+dy[j]*a))
    ans=0
    for position in king_hits:
        if position in queen_hits:
            ans+=1
    print(ans)