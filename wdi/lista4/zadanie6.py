def fib1(n,r):
    a= 1%r
    b= 1%r
    for i in range(2,n+1):
        a,b = b,(a+b)%r
    return b

print(fib1(0,3))