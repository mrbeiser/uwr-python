
def usun(n, a,b):
    return n[:a] + n[b:]

def usun_w_nawiasach(s):
    wypisuj = True

    for i in s:
        if i == '(':
            wypisuj = False
        if i == ')':
            i = ''
            wypisuj = True
        if wypisuj:
            print(i, end='')

usun_w_nawiasach('Ala ma kota (perskiego) aaa(aaaaaaaaaaaaaaaaaaaaaaaa) ()')