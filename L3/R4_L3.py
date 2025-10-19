carros = ['Fiat', 'Chevrolet', 'Ford', 'Honda']
print(f"Lista original: {carros}")

# Adiciona a marca Jeep na segunda posição da lista
# A segunda posição corresponde ao índice 1
carros.insert(1, 'Jeep')
print(f"Após adicionar 'Jeep': {carros}")

# Apaga o último registro da lista
carros.pop()
print(f"Após apagar o último registro: {carros}")

# Adiciona a marca Toyota a última posição da lista
carros.append('Toyota')
print(f"Após adicionar 'Toyota': {carros}")

# Mostra quantos elementos possui a lista
print(f"A lista possui {len(carros)} elementos.")

# Ordena a lista
carros.sort()
print(f"Lista ordenada: {carros}")