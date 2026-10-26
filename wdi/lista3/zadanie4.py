def dzielnikizpotega(n,k):
    listanajwiekszychp = []
    najwiekszep = 0
    for i in range(k):
        a = int(input())
        m = n
        p = 0
        while m%a == 0:
            m//=a
            p+=1

        if p == najwiekszep and p > 0:
            listanajwiekszychp.append(a)
        elif p>najwiekszep:
            listanajwiekszychp = [a]
            najwiekszep = p

    return najwiekszep,listanajwiekszychp

print(dzielnikizpotega(63000,3))