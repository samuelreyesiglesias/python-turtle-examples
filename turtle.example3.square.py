#importamos
from turtle import *
 
 #configuramos lineas y colores
bgcolor("green")  
pencolor("white") 
pensize(10) 

#linea 100px a derecha
forward(100) #ejemplo de la primer linea
#90 gradis a la izquierda
left(90) #cambiamos la direccion
# # 100px a la derecha
forward(100) #dibujamos en esa direccion, en este caso hacia arriba porque habiamos rotado en 90 grados
# # 90 gradis a la izquierda
left(90) # aqui rotamos
# #   100px a la derecha
forward(100)
# #  seteamos 90 gradis a la izquierda
left(90) #rotamos hacia abajo
# # 100px a la derecha
forward(100) #y dibujamos
# #rotamos 90 grados a la izquierda
 #listo
 


done()
#para ejecutar el programa se debe de abrir la terminal y escribir el siguiente comando
#python turtle.example3.square.py
