'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

n=int(input())
score_board=list(map(int,input().split()))
maxi=score_board[0]
mini=score_board[0]
res=0
for i in score_board:
    if i>maxi:
        res+=1
        maxi=i
    elif i<mini:
        res+=1
        mini=i
print(res)