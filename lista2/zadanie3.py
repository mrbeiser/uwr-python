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
            kolko(kolka[i], len(kolka)-i)


ogarodstep([5,7,9])