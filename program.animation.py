from turtle import *
#import library for use colors
from colorsys import * 

speed(0)
def animate():
    for j in range(30):
        for i in range(4):
            color(hsv_to_rgb(i/4,1,1))
            forward(100-j)
            circle(10)
            circle(10,180)
            circle(100-j,90)
            right(90-j)

animate()
