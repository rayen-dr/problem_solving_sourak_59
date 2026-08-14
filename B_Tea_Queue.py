'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n=int(input())
    st=[]
    for i in range(n):
        l,r=map(int,input().split())
        st.append((l,r))
    curr_time=0
    result=[]
    for (l,r)in st:
        if curr_time<l:
            curr_time=l
        if curr_time<=r:
            result.append(curr_time)
            curr_time+=1
        else:
            result.append(0)
    print(*result)