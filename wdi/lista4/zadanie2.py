def reprezentacjasilniowa(n):
    returnstring = ""

    #dzielnik
    d=2
    while n>0:
        if d>2:
            returnstring+="+ "


        returnstring += f"{str(d-1)}! * {str(n%d)} "
        n = n // d
        d+=1

    return returnstring

print(reprezentacjasilniowa(100))