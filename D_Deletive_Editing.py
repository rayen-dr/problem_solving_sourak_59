'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    s,t=map(str,input().split())
    n=len(s)
    m=len(t)
    frequency_in_t=[0]*26
    for char in t:
        frequency_in_t[ord(char)-ord('A')]+=1
    final_string=[]
    for i in range(n-1,-1,-1):
        if frequency_in_t[ord(s[i])-ord('A')]>0:
            frequency_in_t[ord(s[i])-ord('A')]-=1
            final_string.append(s[i])
    final_string.reverse()
    if ''.join(final_string)==t:
        print("YES")
    else:
        print("NO")