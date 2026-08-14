''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    answer=False
    new_a=2*b-c
    if new_a/a>0 and new_a%a==0:
        answer=True
    new_b=(a+c)/2
    if new_b/b>0 and new_b%b==0 and (c-a)%2==0:
        answer=True
    new_c=2*b-a
    if new_c/c>0 and new_c%c==0:
        answer=True
    if answer:
        print("YES")
    else:
        print("NO")