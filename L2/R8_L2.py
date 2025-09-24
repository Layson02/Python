faixa_0_25 = 0
faixa_26_60 = 0     #declarando o começo de cada variavel 
faixa_maior_60 = 0
while True:
    entrada = input("Digite uma idade (ou 'x' para parar): ")

    if entrada.lower() == 'x': # O ".lower()" converte a entrada para minúscula, aceitando 'x' ou 'X'
        print("Finalizando a entrada de dados...")
        break # Interrompe o laço while
    try:
        idade = int(entrada) #  Se não for 'x', tenta converter para número
        if idade < 0:
            print("Idade inválida. Por favor, insira um número positivo.")
            continue # "continue" pula para a próxima iteração do laço
        if 0 <= idade <= 25:
            faixa_0_25 += 1
        elif 26 <= idade <= 60:
            faixa_26_60 += 1
        else:
            faixa_maior_60 += 1
            

    except ValueError: #caso o usuario meta um negocio nada aver
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("\n--- Resultado da Contagem ---")
print(f"Pessoas com idade entre 0 e 25 anos: {faixa_0_25}")
print(f"Pessoas com idade entre 26 e 60 anos: {faixa_26_60}")
print(f"Pessoas com idade maior que 60 anos: {faixa_maior_60}")