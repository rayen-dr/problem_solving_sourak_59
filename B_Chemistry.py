''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    frequency_of_characters=[0]*26
    for char in s:
        frequency_of_characters[ord(char)-ord('a')]+=1
    odd_frequency=0
    for freq in frequency_of_characters:
        odd_frequency+=freq%2
    if odd_frequency>k+1:
        print("NO")
    else:
        print("YES")