
n1 = int(input("Digite o primeiro valor inteiro: "))
n2 = int(input("Digite o segundo valor inteiro: "))

soma = n1 + n2

if soma % 2 == 0:
    print(f"A soma é {soma}. O resultado é par")
else:
    print(f"A soma é {soma}. O resultado é impar")