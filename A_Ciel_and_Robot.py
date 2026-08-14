'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''
     
def check(el,dx,dy):
    if el=='R':
        dx+=1
    elif el=='L':
        dx-=1
    elif el=='U':
        dy+=1
    else:
        dy-=1
    return dx,dy

a,b=map(int,input().split())
s=input()
dx=0
dy=0
for el in s:
    dx,dy=check(el,dx,dy)
B=False
x=0
y=0
if a==0 and b==0:
    B=True
for el in s:
    x,y=check(el,x,y)
    if dx==0 and dy==0:
        if x==a and y==b:
            B=True
    elif dx==0:
        if x==a and dy!=0 and (b-y)%dy==0 and (b-y)//dy>=0:
            B=True
    elif dy==0:
        if y==b and dx!=0 and (a-x)%dx==0 and (a-x)//dx>=0:
            B=True
    else:
        if (a-x)*dy==(b-y)*dx and (a-x)%dx==0 and (b-y)%dy==0:
            k1=(a-x)//dx
            k2=(b-y)//dy
            if k1==k2 and k1>=0:
                B=True
if B:
    print("Yes")
else:
    print("No")