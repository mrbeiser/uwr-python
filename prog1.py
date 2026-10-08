

def potega(a,n):
    wynik = 1  # zmienna lokalna
    for i in range(n):
       wynik = wynik * a   # albo: wynik *= a
    return wynik
   
def kwadrat(n):
    for i in range(n):
       for j in range(n):   # pętla w pętli
          print ("*", end=" ")
       print()
      
def kwadrat2(n):
    for i in range(n):
       print (n * "#")      
  
# wcześniej były definicje, poniżej jest część która się wykonuje
print ()

for i in range(10):
    print ("Przebieg:",i)
    print (20 * "-")
    if i <=4:
        kwadrat(3+2*i)
    else:
        kwadrat2(3+(i-5))
    print()    # pusty wiersz   
         
     
   
