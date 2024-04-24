from turtle import * 
from math import *
from random import *

size=1
actual_color_index = 0
speed(0)
j=50
 

 
for i in range(100):  
        pensize(randint(0,10))
        right(randint(0,360))  
        forward(randint(0,100))
        circle(randint(0,100), randint(0, 360))
 
    
done()
