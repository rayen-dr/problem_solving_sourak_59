''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    s_sorted=sorted(s)
    if s==''.join(s_sorted):
        print("Bob")
        continue
    c0=s.count('0')
    res=[]
    for i in range(c0):
        if s[i]=='1':
            res.append(i+1)
    for i in range(c0,n):
        if s[i]=='0':
            res.append(i+1)
    print("Alice")
    print(len(res))
    print(*res)
    
        