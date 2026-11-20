def usun_duplikaty(L):

    pary = []
    for i in range(len(L)):
        pary.append((L[i], i))
    pary.sort()

    pierwsze = []
    for i in range(len(pary)):
        if i==0 or pary[i][0] != pary[i-1][0]:
            pierwsze.append((pary[i][1], pary[i][0]))
    pierwsze.sort()

    wynik = []
    for indeks,wartosc in pierwsze:
        wynik.append(wartosc)

    return wynik

print(usun_duplikaty([1,2,3,1,2,3,8,2,2,2,9,9,4]))

