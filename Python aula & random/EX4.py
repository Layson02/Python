operacao = input("insira o simbolo da operação")
valor1 = int(input("insira o valor")) #pode ser float para frações e flexibilidade
valor2 = int(input("insira o valor")) #pode ser float para frações e flexibilidade
if operacao == "1":
 print(valor1 + valor2)
elif operacao == "2":
 print(valor1 - valor2)
elif operacao == "3":
 print(valor1 * valor2)
elif operacao == "4":
 print(valor1 / valor2)

