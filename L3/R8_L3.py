valores = [1, 2, 3, 4, 5, 6, 7, 8]

# O operador % (módulo) retorna o resto da divisão. Se for 0, o número é par.
pares = [v for v in valores if v % 2 == 0]

print(f"A lista apenas com os valores pares é: {pares}")