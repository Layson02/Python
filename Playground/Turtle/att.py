import turtle

# Configurar a tela
tela = turtle.Screen()
tela.bgcolor("white")

# Configurar a tartaruga
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.speed(0)  # Velocidade máxima
tartaruga.color("red")

# Função para desenhar o coração
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

# Tornar a tartaruga invisível
tartaruga.penup()
tartaruga.goto(0, -100)  # Posicionar a tartaruga no centro da tela
tartaruga.pendown()
tartaruga.hideturtle()  # Tornar a tartaruga invisível durante o desenho

# Desenhar o coração
desenhar_coracao()

# Exibir a tartaruga novamente
tartaruga.showturtle()

# Adicionar um nome ou título no meio do coração
nome = turtle.textinput("Nome", "Digite um nome ou título:")
tartaruga.penup()
tartaruga.goto(0, 0)  # Posicionar a tartaruga no centro vertical do coração
tartaruga.pendown()
tartaruga.color("black")
tartaruga.write(nome, align="center", font=("Arial", 16, "normal"))

# Finalizar
tela.exitonclick()
