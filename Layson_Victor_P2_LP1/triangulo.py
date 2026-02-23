x = float(input("Insira o valor da medida de um dos lados: "))
y = float(input("Insira o valor da medida de um dos lados: "))
z = float(input("Insira o valor da medida de um dos lados: "))

if x + y > z and x + z > y and y + z > x:
    print("O triângulo é válido.")
    
    if x == y == z:
        print("Triângulo equilátero.")
    elif x != y and x != z and y != z:
        print("Triângulo escaleno.")
    else:
        print("Triângulo isósceles.")
else:
    print("Triângulo inválido.")