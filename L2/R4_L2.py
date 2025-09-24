adm = "admin"
adm_pass = "admin1"
login = input("Digite o seu login: ")
senha = input("Digite a sua senha: ")
if login == adm and senha == adm_pass:
    print("Você está logado.")
else:
    print("Login ou senha incorretos.")