def sprawdzpalindrombinarny(n):
    binarna = liczbanabinarna(int(n))
    print(binarna)
    if binarna == binarna[::-1]:
        return True

    return False

def liczbanabinarna(n):
    if n == 0:
        return "0"
    wynik = ""
    while n > 0:
        wynik = str(n%2) + wynik
        n //= 2

    return wynik
print(sprawdzpalindrombinarny(input()))