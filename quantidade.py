while True:
    try:
        quantidade = int(input("Digite a quantidade de produtos: "))

        if 1 <= quantidade:
            break
        else:
            print("O número de produtos deve ser maior que 1.")
    except ValueError:
        print("Digite um número válido")

print("Quantidade registrada! ", quantidade)