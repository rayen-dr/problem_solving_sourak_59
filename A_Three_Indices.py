''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

import math
t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    flag=False
    for j in range(1,n-1):
        i=-1
        k=-1
        for left in range(j):
            if p[left]<p[j]:
                i=left
                break
        for right in range(j+1,n):
            if p[right]<p[j]:
                k=right
                break
        if i!=-1 and k!=-1:
            print("YES")
            print(i+1,j+1,k+1)
            flag=True
            break
    if not flag:
        print("NO")
