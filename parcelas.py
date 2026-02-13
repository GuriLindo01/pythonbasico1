while True:
    try:
        parcela = int(input("Digite um número de parcelas "))

        if 1 <= parcela <= 12:
            break
        else:
            print("As parcelas devem ser entre 1 e 12.")
    except ValueError:
        print("Digite apenas números")

print("Parcelas registradas! ", parcela)