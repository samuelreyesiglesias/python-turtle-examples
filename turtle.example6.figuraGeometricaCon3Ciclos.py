#importamos lib
from turtle import *

#velocidad maxima 
speed(0)
pencolor("red")
colores = ("red", "green", "blue")
#hacemos 3 ciclos
for x in range(100):
    for j in range(14):
        for i in range(4):
            #aqui damos vida a dibujar las lineas que vaya siendo dinamico un 
            forward(100-i)
            left(40-i)
            pencolor(colores[i%3])
            # left(25) 
            # circle(100-j)

done()