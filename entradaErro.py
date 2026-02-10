while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade <=0:
            print("A idade dever maior que zero.")
        else:
            break
    except ValueError:
        print("Digite apenas números inteiros.")

print("idade Cadastrada: ",idade)