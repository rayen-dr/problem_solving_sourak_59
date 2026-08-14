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
    b=list(map(int,input().split()))
    longest_subarray_a=[0]*(2*n+1)
    longest_subarray_b=[0]*(2*n+1)
    counter=1
    for i in range(1,n):
        if a[i]==a[i-1]:
            counter+=1
        else:
            longest_subarray_a[a[i-1]]=max(longest_subarray_a[a[i-1]],counter)
            counter=1
    longest_subarray_a[a[n-1]]=max(longest_subarray_a[a[n-1]],counter)  
    counter=1
    for i in range(1,n):
        if b[i]==b[i-1]:
            counter+=1
        else:
            longest_subarray_b[b[i-1]]=max(longest_subarray_b[b[i-1]],counter)
            counter=1
    longest_subarray_b[b[n-1]]=max(longest_subarray_b[b[n-1]],counter)
    max_freq=-1
    for i in range(1,2*n+1):
        max_freq=max(max_freq,longest_subarray_a[i]+longest_subarray_b[i])
    print(max_freq)