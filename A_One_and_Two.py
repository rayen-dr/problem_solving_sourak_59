''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    tot_nb_of_twos=a.count(2)
    current_nb_of_twos=0
    ans=-1
    for i in range(n):
        if a[i]==2:
            current_nb_of_twos+=1
        if current_nb_of_twos==(tot_nb_of_twos-current_nb_of_twos):
            ans=i+1
            break
    print(ans)