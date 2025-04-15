senha = "cdd123"
tentativa = input("Senha: ")
contador = 0
while tentativa != senha and contador <= 1:
    tentativa = input("Senha incorreta Digite novamente: ")
    contador += 1
if tentativa == senha:
    print("Acesso Permitido")
else:
    print("Acesso negado")