# wejscie - n liczba naturalna
# wyjscie - wynik dzialania suma od i do n, -1 do potegi i przez i
# zlozonosc czasowa O(n)
# zlozonosc pamieciowa O(1)

n = int(input())
suma = 0
for i in range(1, n+1):
    suma += ((-1)**i)/i

print(suma)