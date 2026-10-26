def kcyfrowaliczba(n):
    #listaliczb = [int(i) for i in str(n)]
    listaliczb = []

    while n > 0:
        listaliczb.append(n%10)
        n//=10

    return len(set(listaliczb))

print(kcyfrowaliczba(7777))