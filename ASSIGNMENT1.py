import turtle
init = 20
turtle.color('red')
for i in range(1,11):
    turtle.penup()
    turtle.goto(0,-init*i)
    turtle.pendown()

    turtle.circle(init*i)

