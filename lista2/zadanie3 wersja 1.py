import math
from math import dist
def kolko(n,add):

    for i in range(n):
        print(add * " ", end='')
        for j in range(n):
            printchar = " "
            if add != 0 and i==n:
                continue
            if i <= n//2:
                if n//2 - i - (n//2 / 2) <= j <= n//2 + i + (n//2 / 2):
                    printchar = "#"
                print(printchar, end='')
            else:
                if i - n//2 - (n//2 / 2) <= j <= n - (i - n//2 +1) + (n//2 / 2):
                    printchar = "#"

                print(printchar, end='')
        print()


def ogarodstep(kolka):
    for i in range(len(kolka)):
            kolkozdlugoscia(kolka[i], max(kolka)//2 - (kolka[i] // 2))


# ogarodstep([5,25,41])

def kolkozdlugoscia(n, add):
    radius = n/2
    center = (n-1)/2

    for i in range(n):
        print(add * " ", end='')
        for j in range(n):
            printchar = " "
            if math.dist((center,center), (i,j)) < radius:
                printchar = "#"
            print(printchar, end='')
        print()


ogarodstep([15,17,99])