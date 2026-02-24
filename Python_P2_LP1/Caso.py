respostas_positivas = 0

ask1= input("1. Telefonou para a vítima? (S/N): ").strip().upper()
if ask1 == 'S': respostas_positivas += 1

ask2 = input("2. Esteve no local do crime? (S/N): ").strip().upper()
if ask2 == 'S': respostas_positivas += 1

ask3 = input("3. Mora perto da vítima? (S/N): ").strip().upper()
if ask3 == 'S': respostas_positivas += 1

ask4 = input("4. Devia para a vítima? (S/N): ").strip().upper()
if ask4 == 'S': respostas_positivas += 1

ask5 = input("5. Já trabalhou com a vítima? (S/N): ").strip().upper()
if ask5 == 'S': respostas_positivas += 1

if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")