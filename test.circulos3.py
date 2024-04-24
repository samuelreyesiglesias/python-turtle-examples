import turtle as t

t.pensize(2)
t.pencolor("red")
t.speed(0)
for i in range(50):
    t.circle(i*10,-25)
    t.circle(i*-10,25)
    t.forward(-10)
    t.forward(20) 
    t.circle(20)

done();