from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
    iloscznakow = n
    print(f'Dla {n}: ', end='')
    while iloscznakow > 0:
        if iloscznakow == 0:
            break

        text = losuj_fragment()
        while (len(text)>iloscznakow) or (iloscznakow - len(text)) == 1:
            text = losuj_fragment()

        print(text, end=' ')
        iloscznakow -= len(text)
    print()


for i in range(10):
    losuj_haslo(8)
    losuj_haslo(12)

