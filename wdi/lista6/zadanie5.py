from wdi import *

def sito(n):
    s = Array(n+1)
    s[0]=0
    s[1]=0

    for i in range(2,n+1):
        s[i] = 1 # czyli sa kandydatami
    p=2
    while p*p<=n:
        if s[p]==1:
            j=p*p
            while j<=n:
                s[j] = 0
                j+=p
        p = p+1
    return s


def printsito(sito):
    for x in range(len(sito)):
        if sito[x]==1:
            print(x)

printsito(sito(30))