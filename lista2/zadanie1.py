def szachownica(n,k):
    squareCount = 2*n

    currentColor = False # dla spacji 0 czyli kolor bialy, dla \# wartosc 1 czyli kwadraciki czarne

    for m in range(squareCount): # liczba kwadratow
        for o in range(k): #liijka kwadratu
            for i in range(squareCount): # kolumna kwadratu
                for j in range(k):
                    print(zwrocZnak(currentColor), end='')

                currentColor = not currentColor
            print()
        currentColor = not currentColor

def zwrocZnak(color):
    if color:
        return "#"
    else:
        return " "

szachownica(3,5)