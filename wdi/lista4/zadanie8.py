from wdi import *

def najmniejsza(n, m):

    t = 1
    pomocnicza = n
    while pomocnicza < m:
        pomocnicza *= pomocnicza
        t+=1

    potegi = Array(t+1)
    potegi[0] = n

    for i in range(1, t + 1):
        potegi[i] = potegi[i - 1] * potegi[i - 1]


    k=0
    p=1

    for i in range(t-1, -1, -1):
        k = 2*k
        if p * potegi[i] < m:
            p = p * potegi[i]
            k = k + 1
    return k + 1

print(najmniejsza(2, 33))