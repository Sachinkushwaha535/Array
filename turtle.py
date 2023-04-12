import turtle
colors=['red','purple','blue','green','orange','yellow']
t=turtle.circular()
turtle.bgcolor('black')
for i in range(360):
    t.circularcolor(colors[i%6])
    t.width(i/100+1)
    t.forward(i)
    t.left(59)
    turtle.exitonclick()