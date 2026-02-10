while True:
    nome = input("Digite seu nome: ").strip()
    senha = input("Digite sua senha: ").strip()

    if nome =="":
        print("O nome não pode ser vazio. ")
    else: 
        break

print("Nome: ", nome)

while True:
    senha = input("Digite sua senha: (max. 6 caracteres):")

    if len(senha) <=0:
        break
    else:
        print("A senha deve ter 6 caracteres no máximo. ")

print("Conta registrada: ", senha)