from turtle import *
speed(-1) # fastest
side = 20
for i in range(side):
    for i in range(side):
        for i in range (side):
            fd(25)
            lt(360/side)
            dot(2)
        fd(50)
        lt(360/side)
    fd(100)
    lt(360/side)
hideturtle()
mainloop()            