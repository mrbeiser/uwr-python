# wejscie - a,b liczby naturalne
# wyjscie - nww liczb a,b
# zlozonosc czasowa O(log2 (n + m))
#

# a b to liczby naturalne
def nww(a,b):
    return a*b//nwd(a,b)


def nwd(a,b):
    if a < b:
        (a,b) = (b,a)
    while b > 0:
        k = a%b
        a = b
        b = k
    return a


def najmniejszyulamek(a,b):
    d = nwd(a,b)
    print(f"{a//d}/{b//d}")

def przypadkitestowe():
    najmniejszyulamek(12, 18)   # → (2, 3)
    najmniejszyulamek(4, 12)    # → (1, 3)
    najmniejszyulamek(5, 7)     # → (5, 7)    już nieskracalny
    najmniejszyulamek(6, 6)     # → (1, 1)
    najmniejszyulamek(7, 1)     # → (7, 1)
    najmniejszyulamek(1, 5)     # → (1, 5)
    najmniejszyulamek(100, 25)  # → (4, 1)
    najmniejszyulamek(18, 12)   # → (3, 2)    licznik większy od mianownika
    najmniejszyulamek(17, 34)   # → (1, 2)    licznik dzieli mianownik
    najmniejszyulamek(84, 36)   # → (7, 3)


__all__ = ["nwd", "nww"]