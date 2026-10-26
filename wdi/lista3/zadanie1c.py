# wejscie - x,n liczby naturalne
# wyjscie - suma od 1 do n, i razy x do potegi i
# zlozonosc czasowa O(n)
# zlozonosc pamieciowa O(1)

n = int(input())
x = int(input())
suma = 0
for i in range(1, n+1):
    suma += (i*(x**i))

print(suma)