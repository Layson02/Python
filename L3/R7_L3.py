valores = [1, 1, 2, 2, 3, 4, 8, 9, 9]

# Uma forma simples de remover duplicados é converter a lista para um conjunto (set)
# e depois converter de volta para uma lista
lista_sem_duplicados = list(set(valores))

print(f"A lista sem valores duplicados é: {lista_sem_duplicados}")