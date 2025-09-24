valor = int(input("Digite um valor "))

if valor % 2 == 0:
    print(f"O número {valor} é par. valores pares de zero até o valor informado ")
    for i in range(0, valor + 1, 2):
        print(i)
else:
    print(f"O número {valor} é impar. valores ímpares de 1 ao valor informado ")
    for i in range(1, valor + 1, 2):
        print(i)