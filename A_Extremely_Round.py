''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

def check(x):
    count_of_digits=0
    count_of_zeros=0
    while x>0:
        if x%10==0:
            count_of_zeros+=1
        count_of_digits+=1
        x//=10
    return count_of_zeros==count_of_digits-1
roun_numbers=[]
for i in range(1,1000000):
    if check(i):
        roun_numbers.append(i)
           
t=int(input())
for _ in range(t):
    n=int(input())
    ans=0
    for round_number in roun_numbers:
        if round_number<=n:
            ans+=1
        else:
            break
    print(ans)