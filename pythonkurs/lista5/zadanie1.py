def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def srednia(n):
    suma = 0
    for i in range(len(n)):
        suma += n[i]
    return suma/len(n)

def mediana(n):
    posortowana = sorted(n)
    length = len(n)
    if length % 2 == 1:
        return posortowana[length//2]
    else:
        return (posortowana[length//2 - 1] + posortowana[length//2]) / 2

def minmax(n):
    posortowana = sorted(n)
    return f"Minimum: {posortowana[0]}, Maximum: {posortowana[-1]}"

indexcollatza = []
def analiza_collatza(a,b):
    for i in range (a,b+1):
        n = i
        iledocollatza = 0
        while n != 1:
            n = F(n)
            iledocollatza += 1

        indexcollatza.append(iledocollatza)
    print("Srednia: ", srednia(indexcollatza))
    print("Mediana: ", mediana(indexcollatza))
    print(minmax(indexcollatza))

analiza_collatza(3,10)