def conversor(valor):
    valor_convertido = valor * 5.09
    return valor_convertido
print("------PRODUTOS------")
print("1 - notebook (US$750,00)")
print("2 - smartwatch (US$75,00)")
produto = int(input("informe o numero do produto "))

if produto == 1:
    valor_produto = conversor(750.00)
elif produto == 2:
    valor_produto = conversor(75.00)

print(f"valor convertido: R$ {valor_produto}")