from duze_cyfry import daj_cyfre

#for r in daj_cyfre(5):
#    print(r)

def dlcver1(liczba):
    listaliczba = [int(x) for x in str(liczba)]

    for i in listaliczba:
        for r in daj_cyfre(i):
            print(r)

def dlcver2(liczba):
    listaliczba = [int(x) for x in str(liczba)]

    #wczytanie duzych numerow do listy
    for i in range(len(listaliczba)):
        listaliczba[i] = daj_cyfre(listaliczba[i])

    for i in range (len(listaliczba[0])):
        tempstr = ""
        for j in range (len(listaliczba)):
            tempstr += str(listaliczba[j][i]) + " "
        print(tempstr)




dlcver2(123)