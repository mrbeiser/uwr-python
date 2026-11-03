# (a) najwięcej mnożeń będzie przy (2^(k+1))-1 bo działamy na liczbach
# binarnych i najwieksza ilosc jedynek (czyli tez naszych mnozen) bedzie miec liczba
# dokladnie o 1 mniejsza niz maksymalna, daje dokładnie 2(k+1) mnożeń
#
# (b) najmniej mnozen bedzie przy (2^(k)) bo mamy wtedy najmniejsza liczbe zawierajaca najmniejsza
# liczbe jedynek czyli tez liczbe z najmniejsza iloscia dzialan (bo nie wchodzimy do ifa)
# co daje k+2 mnożeń


def szybkiepotegowanie(a,b):
    rez = 1
    iledzialan = 0
    while b>0:
        if b % 2 == 1:
            rez = rez * a
            iledzialan+=1


        b = b // 2
        a = a * a
        iledzialan+=1
    return iledzialan


print(szybkiepotegowanie(2,8192))