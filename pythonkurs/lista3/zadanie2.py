from itertools import product

def replaceindexinstring(st,index, new):
    lista = list(st)
    lista[index] = str(new)
    return "".join(lista)
def sprawdzPierwsza(n, ilosccyfer):
    if len(str(n)) != ilosccyfer:
        return False

    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def generujzbiorsiodemek(iloscsiodemek, ilosccyfer):
    wolnemiejsca = ilosccyfer-iloscsiodemek+1
    siodemki = iloscsiodemek*"7"

    liczby = []

    for step in range(wolnemiejsca):
        for cyfry in product('0123456789', repeat=wolnemiejsca-1):
            tekst = ''.join(cyfry[:step]) + siodemki + ''.join(cyfry[step:])

            wypisac = True
            for i in range (wolnemiejsca-1):
                if tekst[i] == 0:
                    wypisac = False

            if wypisac:
                liczby.append(tekst)

    return list(set(liczby))
def hiperSzczesliweLiczby(iloscsiodemek,ilosccyfer):
    ilesiodemek = 0
    for i in generujzbiorsiodemek(iloscsiodemek, ilosccyfer):
            if sprawdzPierwsza(int(i), ilosccyfer):
                ilesiodemek += 1

    print(ilesiodemek)

hiperSzczesliweLiczby(5,10)


