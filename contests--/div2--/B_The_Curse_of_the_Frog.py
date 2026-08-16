''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    land=0
    target=-float('inf')
    for _ in range(n):
        a,b,c=map(int,input().split())
        land+=(b-1)*a
        k_ci_ai=a*b-c
        target=max(target,k_ci_ai)
    if target>=x:
        print("0")
        continue
    if target<=0:
        print("-1")
        continue
    diff=x-land 
    res=(diff+target-1)//target
    print(res)