''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

def analogie(ch,x):
    return all(x[i]=='?' or x[i]==ch[i] for i in range(len(x)))

t=int(input())
for _ in range(t):
    n=int(input())
    x=input()
    if (n%2==1)and x[0]=='b':
        print("NO")
        continue
    ok=True
    for i in range(n%2,n,2):
        if x[i]!='?' and x[i+1]!='?' and x[i]==x[i+1]:
            print("NO")
            ok=False
            break
    if ok:
        print("YES")
        