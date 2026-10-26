def krzyzyk(n):

    for a in range(n*3):
        printchar = '*'

        for i in range(3):
            for j in range(n):
                if i in [0,2] and (a in range (0,n) or a in range (n*3-n, n*3)):
                    printchar = ' '
                else:
                    printchar = '*'
                print(printchar, end='')

        print()



krzyzyk(5)