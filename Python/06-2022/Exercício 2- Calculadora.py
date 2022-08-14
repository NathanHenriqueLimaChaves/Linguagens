print("Bem vindo(a) a calculadora flash!\n")
while True:
    try:
        print("[1]Soma",
              "[2]Subtração",
              "[3]Multiplicação",
              "[4]Divisão",
              "[5]Sair\n")
        escolha = int(input("Escolha uma das opções acima?"))
        if(escolha == 1):
                print("Soma escolhida!")
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
                soma = (numero1 + numero2)
                print(f"A soma dos número é igual a: {soma}\n")
                print("Deseja realizar outra operação? ;)")
        elif(escolha == 2):
                print("Subtração escolhida!")
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
                subtracao = (numero1 - numero2)
                print(f"A subtração dos números é igual a: {subtracao}\n")
                print("Deseja realizar outra operação? ;)")
        elif(escolha == 3):
                print("Multiplicação escolhida!")
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
                multiplicacao = (numero1 * numero2)
                print(f"A multiplicação dos números é igual a: {multiplicacao}\n")
                print("Deseja realizar outra operação? ;)")
        elif(escolha == 4):
                print("Divisão escolhida!")
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))
                divisao = (numero1 / numero2)
                print(f"A divisão dos números é igual a: {divisao}\n")
                print("Deseja realizar outra operação? ;)")
        elif(escolha == 5):
                print("Volte sempre! :)")
                break
        else:
                print("Opção inválida! Tente novamente.\n")
    except ValueError:
        print("Você digitou algo errado! Tente novamente.\n")
