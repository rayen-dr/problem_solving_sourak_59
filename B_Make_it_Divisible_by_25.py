''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

def min_operations(n,possible_value):
    op=0
    checker_index=len(possible_value)-1
    for i in range(len(n)-1,-1,-1):
        if n[i]==possible_value[checker_index]:
            checker_index-=1
            if checker_index<0:
                break
        else:
            op+=1
    if checker_index>=0:
        op=float('inf')
    return op

possible_value=["00","25","50","75"]
t=int(input())
for _ in range(t):
    n=input()
    ans=float('inf')
    for possible_val in possible_value:
        ans=min(ans,min_operations(n,possible_val))
    print(ans)
    
    