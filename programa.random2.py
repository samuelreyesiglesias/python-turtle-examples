from turtle import * 
from math import *
from random import *

size=1
actual_color_index = 0
speed(0)
j=50
 

 
for i in range(20):  
        # pensize(randint(0,10))
        # right(randint(0,360))  
        right(j-i) # j-i is the angle of the rotation
        forward(15)
        circle(1)
 
    
done()
