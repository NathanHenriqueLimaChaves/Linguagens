try:
    print("Bem vindo(a) a caluladora detalhista!\n")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    print("Agora escolha qual operação deseja realizar:")
    escolha = int(input("[1] Adição  [2] Subtração  [3]Multiplicação  [4] Divisão  [5] Exponenciação  [0] Sair\n Sua escolha: "))
    if(escolha == 0):
        print("Volte sempre! :)")
    elif(escolha == 1):
        print("Você escolheu adição!")
        adicao = numero1 + numero2
        print(f"O resultado da adição entre {numero1} e {numero2} é: {adicao}. Alguns fatos sobre o resultado:")
        if(adicao%2 == 0):
            print("1)O número é par;")
        else:
            print("1)O número é ímpar;")
        if(adicao > 0):
            print("2)O número é positivo;")
        elif(adicao == 0):
            print("2)O número é igual a 0;")
        else:
            print("2)O número é negativo;")
        round_adc = round(adicao)
        if(adicao == round_adc):
            print("3)O número é inteiro.")
        else:
            print("3)O número é decimal.")
    elif(escolha == 2):
        print("Você escolheu subtração!")
        subtracao = numero1 - numero2
        print(f"O resultado da subtração entre {numero1} e {numero2} é: {subtracao}. Alguns fatos sobre o resultado:")
        if(subtracao%2 == 0):
            print("1)O número é par;")
        else:
            print("1)O número é ímpar;")
        if(subtracao > 0):
            print("2)O número é positivo;")
        elif(subtracao == 0):
            print("2)O número é igual a 0;")
        else:
            print("2)O número é negativo;")
        round_sub = round(subtracao)
        if(subtracao == round_sub):
            print("3)O número é inteiro.")
        else:
            print("3)O número é decimal.")
    elif(escolha == 3):
        print("Você escolheu multiplicação!")
        multiplicacao = numero1*numero2
        print(f"O resultado da multiplicação entre {numero1} e {numero2} é: {multiplicacao}. Alguns fatos sobre o resultado:")
        if(multiplicacao%2 == 0):
            print("1)O número é par;")
        else:
            print("1)O número é ímpar;")
        if(multiplicacao > 0):
            print("2)O número é positivo;")
        elif(multiplicacao == 0):
            print("2)O número é igual a 0;")
        else:
            print("2)O número é negativo;")
        round_mult = round(multiplicacao)
        if(multiplicacao == round_mult):
            print("3)O número é inteiro.")
        else:
            print("3)O número é decimal.")
    elif(escolha == 4):
        print("Você escolheu divisão!")
        divisao = numero1/numero2
        print(f"O resultado da divisão entre {numero1} e {numero2} é: {divisao}. Alguns fatos sobre o resultado:")
        if(divisao%2 == 0):
            print("1)O número é par;")
        else:
            print("1)O número é ímpar;")
        if(divisao > 0):
            print("2)O número é positivo;")
        elif(divisao == 0):
            print("2)O número é igual a 0;")
        else:
            print("2)O número é negativo;")
        round_div = round(divisao)
        if(divisao == round_div):
            print("3)O número é inteiro.")
        else:
            print("3)O número é decimal.")
    elif(escolha == 5):
        print("Você escolheu exponenciação!")
        exponenciacao = numero1**numero2
        print(f"O resultado da exponenciação entre {numero1} e {numero2} é: {exponenciacao}. Alguns fatos sobre o resultado:")
        if(exponenciacao%2 == 0):
            print("1)O número é par;")
        else:
            print("1)O número é ímpar;")
        if(exponenciacao > 0):
            print("2)O número é positivo;")
        elif(exponenciacao == 0):
            print("2)O número é igual a 0;")
        else:
            print("2)O número é negativo;")
        round_exp = round(exponenciacao)
        if(exponenciacao == round_exp):
            print("3)O número é inteiro.")
        else:
            print("3)O número é decimal.")
    else:
        print("Escolha indisponível. Tente novamente!")
except ValueError:
    print("Por favor, digite algo válido. Tente novamente.")