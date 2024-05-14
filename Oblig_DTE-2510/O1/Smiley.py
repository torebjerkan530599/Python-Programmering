
import turtle

turtle.home()
turtle.speed(10)
turtle.pensize(3)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-50,150)
turtle.pendown()
turtle.dot(10,"black")
turtle.penup()

turtle.forward(100)
turtle.pendown()
turtle.dot(10,"black")
turtle.penup()

turtle.goto(-65, 80)
turtle.pendown()
turtle.color("black")
turtle.right(60)
turtle.circle(80,120)
turtle.penup()

turtle.hideturtle()
turtle.done()