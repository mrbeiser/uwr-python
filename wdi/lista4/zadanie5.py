def ciagg(n):
    a,b,c = 1,1,3
    for i in range(4,n+1):
        a,b,c = b,c, a+b+c

    return c
print(ciagg(4))