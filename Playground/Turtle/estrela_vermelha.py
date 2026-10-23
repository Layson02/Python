import turtle

# Seleciona a tartaruga e ajusta sua cor
turtle.color("red")

turtle.begin_fill()
# Desenha a estrela
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
    

# finalizacão do preenchimento
turtle.end_fill()
# Mantém a janela aberta até que o usuário feche
turtle.exitonclick()
