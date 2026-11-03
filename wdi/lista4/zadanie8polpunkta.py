# n^k >= m
def najmniejszapotega(n,m):
    k = n+m
    while n**k >= m:
        k = k//2
    return k*k+1

print(najmniejszapotega(2,33))