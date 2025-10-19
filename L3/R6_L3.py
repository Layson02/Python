valores = [10, 20, 30, 40, 50]

# O "for" percorre a cópia, enquanto o "remove" modifica a lista original.
for v in valores[:]:
  if v > 30:
    valores.remove(v)

print(valores)
# Saída: [10, 20, 30]