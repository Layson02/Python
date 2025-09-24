parada = int(input("Digite um valor limite para a sequência de Fibonacci: "))
a, b = 0, 1
sequencia = [] # lista vazia para armazenar depois
while a <= parada:
    sequencia.append(str(a)) # append, vai add o valor convetido para string ao final da lista 
    a, b = b, a + b # "a" ira começar como 0, depois sendo somado com o valor de "b", depois "a" recebe o antigo valor de "b" e "b" recebe o valor dp antigo "a" + "b"  
print(f"A sequência de Fibonacci até {parada} é:")
print(sequencia)