from duze_cyfry import daj_cyfre
import turtle
import random

def generuj_kolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

bong = turtle.Turtle()
turtle.colormode(255)
bong.speed(0)
#for r in daj_cyfre(5):
#    print(r)

def rysujkwadrat():
    bong.begin_fill()
    for i in range(4):
        bong.forward(20)
        bong.left(90)
    bong.end_fill()

def nastepnykwadrat():
    bong.forward(20)


def dlcver1(liczba):
    listaliczba = [int(x) for x in str(liczba)]

    for i in listaliczba:
        startposx, startposy = bong.pos()
        color = generuj_kolor()
        for r in daj_cyfre(i):
            x, y = bong.pos()
            for i in range(len(r)):

                if r[i] == "#":
                    bong.color(color)
                    rysujkwadrat()
                    nastepnykwadrat()
                else:
                    bong.color((255,255,255))
                    rysujkwadrat()
                    nastepnykwadrat()

            bong.teleport(x,y)
            bong.right(90)
            bong.forward(20)
            bong.left(90)
        bong.teleport(startposx+(20*6), startposy)


dlcver1(541)
input()