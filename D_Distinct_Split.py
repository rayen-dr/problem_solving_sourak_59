'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
def prefix_f(s):
    n=len(s)
    p=[0]*(n+1)
    d={}
    for i in range(1,n+1):
        if s[i-1] not in d:
           d[s[i-1]]=1
           p[i]=p[i-1]+1
        else:
            p[i]=p[i-1]
    return p
def suffix_f(s):
    n=len(s)
    p=[0]*(n+1)
    d={}
    for i in range(n-1,-1,-1):
        if s[i] not in d:
           d[s[i]]=1
           p[i]=p[i+1]+1
        else:
            p[i]=p[i+1]
    return p
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    p_f=(prefix_f(s))[1:]
    s_f=(suffix_f(s))[:n]
    res=0
    for i in range(n-1):
       res=max(p_f[i]+s_f[i+1],res) 
    print(res)
    