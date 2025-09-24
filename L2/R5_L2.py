soma_valores = 0
print("Por favor, digite 6 valores.")
for i in range(6):
    valor = float(input(f"Digite o {i+1}º valor: "))
    soma_valores += valor
media = soma_valores / 6
print(f"\nA soma de todos os valores é: {soma_valores}")
print(f"A média dos valores é: {media}")