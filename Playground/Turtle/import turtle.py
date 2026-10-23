import turtle

tela = turtle.Screen()
tela.bgcolor("white")

tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.speed(1)
tartaruga.color("red")

def desenhar_coracao():
    tartaruga.begin_fill()
    tartaruga.left(140)
    tartaruga.forward(224)
    for _ in range(200):
        tartaruga.right(1)
        tartaruga.forward(2)
    tartaruga.left(120)
    for _ in range(200):
        tartaruga.right(1)
        tartaruga.forward(2)
    tartaruga.forward(224)
    tartaruga.end_fill()

tartaruga.penup()
tartaruga.goto(0, -100)
tartaruga.pendown()
desenhar_coracao()

tela.exitonclick()
