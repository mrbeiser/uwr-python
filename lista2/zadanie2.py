def wypiszkoperte(n):
    for i in range(n):
        for k in range(n):
            if i == 0 or i == n - 1:
                print('#', end='')
            else:
                if k == 0 or k == n - 1:
                    print('#', end='')
                elif k == n-i-1 or k == i:
                    print('#', end='')
                else:
                    print (' ', end='')
        print()

wypiszkoperte(10)