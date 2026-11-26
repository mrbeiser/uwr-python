import turtle
from duze_cyfry import daj_cyfre
import random

gridsize = 50
kolory = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black"]
tab = [[0] * gridsize for _ in range(gridsize)]
step = 20

bong = turtle.Turtle()
bong.hideturtle()
turtle.setup(gridsize * step, gridsize * step)
turtle.setworldcoordinates(0, gridsize, gridsize, 0)
turtle.tracer(0)

def randomposxy():
    x = random.randint(0, gridsize-5)
    y = random.randint(0, gridsize-5)
    return x, y

def sprawdzdookola(x, y, kolor):
    if tab[y][x] != 0:
        return False
    if x-1 >= 0 and tab[y][x-1] == kolor: return False
    if x+1 < gridsize and tab[y][x+1] == kolor: return False

    if y-1 >= 0:
        if x-1 >= 0 and tab[y-1][x-1] == kolor: return False
        if tab[y-1][x] == kolor: return False
        if x+1 < gridsize and tab[y-1][x+1] == kolor: return False

    if y+1 < gridsize:
        if x-1 >= 0 and tab[y+1][x-1] == kolor: return False
        if tab[y+1][x] == kolor: return False
        if x+1 < gridsize and tab[y+1][x+1] == kolor: return False
    return True

def pasuje(wzor, x0, y0, kolor):
    for y in range(len(wzor)):
        for x in range(len(wzor[y])):
            if wzor[y][x] == 1:
                if not sprawdzdookola(x0+x, y0+y, kolor):
                    return False
    return True

def wstaw(plansza, cyfra, proby=1000):
    wzor = daj_cyfre(cyfra)
    for _ in range(proby):
        x0, y0 = randomposxy()
        kolor = random.choice(kolory)
        if pasuje(wzor, x0, y0, kolor):
            for y in range(len(wzor)):
                for x in range(len(wzor[y])):
                    if wzor[y][x] == 1:
                        plansza[y0 + y][x0 + x] = kolor
                        rysuj_kwadrat(x0+x, y0+y, kolor)
            return True
    return False

def rysuj_kwadrat(x, y, kolor):
    bong.penup()
    bong.goto(x, y)
    bong.pendown()
    bong.color(kolor)
    bong.begin_fill()
    for dx, dy in [(1, 0), (1, 1), (0, 1), (0, 0)]:
        bong.goto(x + dx, y + dy)
    bong.end_fill()

for i in range(100):
    wstaw(tab, random.randint(0, 9))

turtle.update()
turtle.done()