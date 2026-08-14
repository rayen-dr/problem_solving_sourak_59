'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    largest_substring_length=1
    current_substring_length=1
    for i in range(1,n):
        if s[i]==s[i-1]:
            current_substring_length+=1
        else:
            largest_substring_length=max(largest_substring_length,current_substring_length)
            current_substring_length=1
    largest_substring_length=max(largest_substring_length,current_substring_length)
    print(largest_substring_length+1)
    
    