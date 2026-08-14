'''' اللَّهُمَّ إِنِّي أَسْأَلُكَ مُوجِبَاتِ رَحْمَتِكَ 
        وَعَزَائِمَ مَغْفِرَتِكَ   
    وَالسَّلاَمَةَ مِنْ كُلِّ إِثْمٍ
    والغَنِيمَةَ مِنْ كُلِّ بِرٍّ
        والفَوْزَ بالجَنَّةِ،
     والنَّجاةَ مِنَ النَّارِ '''

import math

x, y, z = map(float, input().split())

def f(base, a, b, nested):
    if base <= 1:
        return -1e100
    if nested:   # base^(a^b)
        return b * math.log(a) + math.log(math.log(base))
    else:        # (base^a)^b
        return a * b * math.log(base)

vals = [
    (f(x,y,z,1), "x^y^z"),
    (f(x,z,y,1), "x^z^y"),
    (f(x,y,z,0), "(x^y)^z"),
    (f(x,z,y,0), "(x^z)^y"),

    (f(y,x,z,1), "y^x^z"),
    (f(y,z,x,1), "y^z^x"),
    (f(y,x,z,0), "(y^x)^z"),
    (f(y,z,x,0), "(y^z)^x"),

    (f(z,x,y,1), "z^x^y"),
    (f(z,y,x,1), "z^y^x"),
    (f(z,x,y,0), "(z^x)^y"),
    (f(z,y,x,0), "(z^y)^x"),
]

if max(x, y, z) > 1:
    print(max(vals)[1])
else:
    print(min(vals)[1])
