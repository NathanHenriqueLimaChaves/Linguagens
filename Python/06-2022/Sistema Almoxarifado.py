print("Sistema Almoxarifado!\n")
estoque_inicial = []
quantidade_10 = []
quantidade_20 = []
quantidade_30 = []
quantidade_40 = []
quantidade_50 = []
while True:
  try:
    continuar = input("Adicionar produto? S/N  ")
    while continuar == 's' or continuar == 'S':
      codigo = int(input("Digite o código do produto: "))
      if(codigo == 10):
        quantidade_10.append(int(input("Agora digite a quantidade: ")))
        continuar = input("Continuar adicionando? S/N  ")
        if(continuar == 's' or continuar == 'S'):
          print("\n")
        elif(continuar == 'n' or continuar == 'N'):
          break
        else:
          print("Comando inválido. Tente novamente!")
      elif(codigo == 20):
        quantidade_20.append(int(input("Agora digite a quantidade: ")))
        continuar = input("Continuar adicionando? S/N  ")
        if(continuar == 's' or continuar == 'S'):
          print("\n")
        elif(continuar == 'n' or continuar == 'N'):
          break
        else:
          print("Comando inválido. Tente novamente!")
      elif(codigo == 30):
        quantidade_30.append(int(input("Agora digite a quantidade: ")))
        continuar = input("Continuar adicionando? S/N  ")
        if(continuar == 's' or continuar == 'S'):
          print("\n")
        elif(continuar == 'n' or continuar == 'N'):
          break
        else:
          print("Comando inválido. Tente novamente!")
      elif(codigo == 40):
        quantidade_40.append(int(input("Agora digite a quantidade: ")))
        continuar = input("Continuar adicionando? S/N  ")
        if(continuar == 's' or continuar == 'S'):
          print("\n")
        elif(continuar == 'n' or continuar == 'N'):
          break
        else:
          print("Comando inválido. Tente novamente!")
      elif(codigo == 50):
        quantidade_50.append(int(input("Agora digite a quantidade: ")))
        continuar = input("Continuar adicionando? S/N  ")
        if(continuar == 's' or continuar == 'S'):
          print("\n")
        elif(continuar == 'n' or continuar == 'N'):
          break
        else:
          print("Comando inválido. Tente novamente!")
  except ValueError:
    print("Comando inválido! Tente novamente.")

  quantidade_inicial10 = int(sum(quantidade_10))
  quantidade_inicial20 = int(sum(quantidade_20))
  quantidade_inicial30 = int(sum(quantidade_30))
  quantidade_inicial40 = int(sum(quantidade_40))
  quantidade_inicial50 = int(sum(quantidade_50))
  print("--------------------------------")
  print("Terminamos de cadastrar os produtos existentes. Vamos para o menu:\n")
  while True:
    print("Escolha a operação:")
    print("[E] Entrada no estoque\n[S] Saída no estoque\n[R] Relatório\n[X] Sair\n")
    escolha = (input("Sua escolha: "))
    if(escolha == 'E' or escolha == 'e'):
      print("Entrada de estoque;\n")
      entrada = int(input("Digite o código do produto: "))
      if(entrada == 10):
        print(f"Atualmente existem {quantidade_inicial10} unidades no estoque!")
        quantidade_entrada = int(input("Digite a quantidade de entrada: "))
        quantidade_inicial10 = quantidade_inicial10 + quantidade_entrada
        print("-----------------------------")
        print("Operação realizada com sucesso!")
        print(f"Agora, o estoque possui {quantidade_inicial10} unidades de caderno!")
        print("-----------------------------")
      elif(entrada == 20):
        print(f"Atualmente existem {quantidade_inicial20} unidades no estoque!")
        quantidade_entrada = int(input("Digite a quantidade de entrada: "))
        quantidade_inicial20 = quantidade_inicial20 + quantidade_entrada
        print("-----------------------------")
        print("Operação realizada com sucesso!")
        print(f"Agora, o estoque possui {quantidade_inicial20} unidades de caneta!")
        print("-----------------------------")
      elif(entrada == 30):
        print(f"Atualmente existem {quantidade_inicial30} unidades no estoque!")
        quantidade_entrada = int(input("Digite a quantidade de entrada: "))
        quantidade_inicial30 = quantidade_inicial30 + quantidade_entrada
        print("-----------------------------")
        print("Operação realizada com sucesso!")
        print(f"Agora, o estoque possui {quantidade_inicial30} unidades de lápis!")
        print("-----------------------------")
      elif(entrada == 40):
        print(f"Atualmente existem {quantidade_inicial40} unidades no estoque!")
        quantidade_entrada = int(input("Digite a quantidade de entrada: "))
        quantidade_inicial40 = quantidade_inicial40 + quantidade_entrada
        print("-----------------------------")
        print("Operação realizada com sucesso!")
        print(f"Agora, o estoque possui {quantidade_inicial40} unidades de borracha!")
        print("-----------------------------")
      elif(entrada == 50):
        print(f"Atualmente existem {quantidade_inicial50} unidades no estoque!")
        quantidade_entrada = int(input("Digite a quantidade de entrada: "))
        quantidade_inicial50 = quantidade_inicial50 + quantidade_entrada
        print("-----------------------------")
        print("Operação realizada com sucesso!")
        print(f"Agora, o estoque possui {quantidade_inicial50} unidades de régua!")
        print("-----------------------------")
      else:
        print("Código inválido!Tente novamente\n")
    elif(escolha == 'S' or escolha == 's'):
      print("Saída de estoque;\n")
      saida = int(input("Digite o código do produto: "))
      if(saida == 10):
        print(f"Atualmente existem {quantidade_inicial10} unidades no estoque!")
        quantidade_saida = int(input("Digite a quantidade de saída: "))
        if(quantidade_inicial10 < quantidade_saida):
          print("Impossível realizar essa retirada! Existem menos produtos no estoque do que o solicitado!\n")
        elif(quantidade_inicial10 >= quantidade_saida):
           quantidade_inicial10 = quantidade_inicial10 - quantidade_saida         
           print("-----------------------------")
           print("Operação realizada com sucesso!")
           print(f"Agora, o estoque possui {quantidade_inicial10} unidades de caderno!")
           print("-----------------------------")
        elif(quantidade_saida <= 0):
          print("Valor inválido. Tente novamente!")
      if(saida == 20):
        print(f"Atualmente existem {quantidade_inicial20} unidades no estoque!")
        quantidade_saida = int(input("Digite a quantidade de saída: "))
        if(quantidade_inicial20 < quantidade_saida):
          print("Impossível realizar essa retirada! Existem menos produtos no estoque do que o solicitado!\n")
        elif(quantidade_inicial20 >= quantidade_saida):
           quantidade_inicial20 = quantidade_inicial20 - quantidade_saida         
           print("-----------------------------")
           print("Operação realizada com sucesso!")
           print(f"Agora, o estoque possui {quantidade_inicial20} unidades de caneta!")
           print("-----------------------------")
        elif(quantidade_saida <= 0):
          print("Valor inválido. Tente novamente!")
      if(saida == 30):
        print(f"Atualmente existem {quantidade_inicial30} unidades no estoque!")
        quantidade_saida = int(input("Digite a quantidade de saída: "))
        if(quantidade_inicial30 < quantidade_saida):
          print("Impossível realizar essa retirada! Existem menos produtos no estoque do que o solicitado!\n")
        elif(quantidade_inicial30 >= quantidade_saida):
           quantidade_inicial30 = quantidade_inicial30 - quantidade_saida         
           print("-----------------------------")
           print("Operação realizada com sucesso!")
           print(f"Agora, o estoque possui {quantidade_inicial30} unidades de lápis!")
           print("-----------------------------")
        elif(quantidade_saida <= 0):
          print("Valor inválido. Tente novamente!")
      if(saida ==40):
        print(f"Atualmente existem {quantidade_inicial40} unidades no estoque!")
        quantidade_saida = int(input("Digite a quantidade de saída: "))
        if(quantidade_inicial40 < quantidade_saida):
          print("Impossível realizar essa retirada! Existem menos produtos no estoque do que o solicitado!\n")
        elif(quantidade_inicial40 >= quantidade_saida):
           quantidade_inicial40 = quantidade_inicial40 - quantidade_saida         
           print("-----------------------------")
           print("Operação realizada com sucesso!")
           print(f"Agora, o estoque possui {quantidade_inicial40} unidades de borracha!")
           print("-----------------------------")
        elif(quantidade_saida <= 0):
          print("Valor inválido. Tente novamente!")
      if(saida == 50):
        print(f"Atualmente existem {quantidade_inicial50} unidades no estoque!")
        quantidade_saida = int(input("Digite a quantidade de saída: "))
        if(quantidade_inicial50 < quantidade_saida):
          print("Impossível realizar essa retirada! Existem menos produtos no estoque do que o solicitado!\n")
        elif(quantidade_inicial50 >= quantidade_saida):
           quantidade_inicial50 = quantidade_inicial50 - quantidade_saida         
           print("-----------------------------")
           print("Operação realizada com sucesso!")
           print(f"Agora, o estoque possui {quantidade_inicial50} unidades de régua!")
           print("-----------------------------")
        elif(quantidade_saida <= 0):
          print("Valor inválido. Tente novamente!")
      else:
        print("Código inválido. Tente novamente!")
    elif(escolha == 'R' or escolha == 'r'):
      print("Relatório;\n")
      print("--------------------------------")
      print("Atualmente, existem no estoque: \n")
      print(f"{quantidade_inicial10} unidades de cadernos;\n{quantidade_inicial20} unidades de canetas;\n{quantidade_inicial30} unidades de lápis;\n{quantidade_inicial40} unidades de borrachas;\n{quantidade_inicial50} unidades de réguas;")
      print("--------------------------------")
    elif(escolha == 'X' or escolha == 'x'):
      print("Volte sempre!")
      break

 