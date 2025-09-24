valor = int(input("Digite um valor inteiro de 0 a 10 para ver sua tabuada: "))
if 0 <= valor <= 10:
    print(f"\n--- Tabuada do {valor} ---")
    for i in range(11):
        resultado = valor * i
        print(f"{valor} x {i} = {resultado}")
else:
    print("Erro!")