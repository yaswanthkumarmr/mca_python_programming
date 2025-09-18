from turtle import *
speed('fast')
pencolor("red")
pensize(3)

side = 45
for i in range(side):
    for i in range(side):
        fd(25)
        lt(360/side)
    fd(10)
    lt(360/side)
hideturtle()
mainloop()    