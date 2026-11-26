def mujsplit(s):
    s = s.strip()
    wynik = []
    slowo = ""
    for znak in s:
        if znak.isspace():
            if slowo:
                wynik.append(slowo)
                slowo = ""
        else:
            slowo += znak
    if slowo:
        wynik.append(slowo)
    return wynik

print(mujsplit("  ala   ma\tkota\n aaaaa a a                         "))