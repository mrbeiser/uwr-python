with open("popularne_slowa2023.txt", "r", encoding="utf-8") as f:
    slowa = f.read().lower().split()
    zbior = set(slowa)

    pary = set()
    for slowo in zbior:
        odwrocone = slowo[::-1]
        if odwrocone in zbior and (odwrocone, slowo) not in pary and (slowo,odwrocone) not in pary:
            pary.add((slowo,odwrocone))

for slowo,odwrocone in pary:
    print(slowo,odwrocone)