def czypierwsza(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n==2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def ZbiorPierwszychDzielnikow(n):
    zbior = set()

    for i in range(1,n+1):
        if n%i == 0 and czypierwsza(i):
            zbior.add(i)

    print(zbior)


ZbiorPierwszychDzielnikow(36)
