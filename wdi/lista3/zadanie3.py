from zadanie2 import *

n = int(input())

def nwddlaciagu(n):
    poprzednia = 0
    for i in range(n):
        aktualna = int(input())
        if i>0:
            poprzednia = nwd(poprzednia,aktualna)
        else:
            poprzednia = aktualna

    return poprzednia

print(nwddlaciagu(n))