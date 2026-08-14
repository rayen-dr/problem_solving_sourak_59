''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    l=list(map(str,input().split()))
    s=input()
    n=int(l[0])
    color=l[1]
    s+=s
    n*=2
    last_green_index=-1
    max_seconds=-float('inf')
    for i in range(n-1,-1,-1):
        if s[i]=='g':
            last_green_index=i
        if s[i]==color:
            max_seconds=max(max_seconds,last_green_index-i)
    print(max_seconds)