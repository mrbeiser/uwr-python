from math import log
from math import floor


for i in range(101):
    result = 1
    for k in range(1, i+1):
            result *= k
    result = floor(log(result)/log(10)) + 1

    if result == 1:
        print(f'{i}! ma {result} cyfrę')
    elif result%10 in [2,3,4] and (result not in[12,13,14]):
        print(f'{i}! ma {result} cyfry')
    else:
        print(f'{i}! ma {result} cyfr')


