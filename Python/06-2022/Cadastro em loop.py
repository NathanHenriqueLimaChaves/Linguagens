print("Digite os seus dados abaixo para completar o registro:\n")
while True:
  try:
    nome = str(input("Nome: "))
    nome_len = len(nome)
    nome_len_int = int(nome_len)
    if(nome_len_int > 0 and nome_len_int <= 3 ):
      print("O nome deve ter mais que TRÊS caracteres.")
      continue
    else:
      idade = int(input("Idade: "))
      if(idade < 0 or idade > 150):
        print("Valor inválido!Tente novamente.")
        continue
      else:
        salario = float(input("Salário: "))
        if(salario <= 0):
          print("Valor inválido")
          continue
        else:
          sexo = str(input("Sexo(M,F ou O): "))
          if(sexo == 'M' or sexo == 'm' or sexo == 'F' or sexo == 'f' or sexo == 'O' or sexo == 'o'):
            estado_civil = str(input("Estado civil(s,c,v ou d): " + "\n"))
            if(estado_civil == 'S' or estado_civil == 's' or estado_civil == 'C' or estado_civil == 'c' or estado_civil == 'V' or estado_civil == 'v' or estado_civil == 'D' or estado_civil == "d"):
              print("Seus dados são:\n")
              print(f"Nome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}\nEstado civil: {estado_civil}")
              break
          else:
            print("Opção inválida!")
            continue         
  except ValueError:
    print("Por favor, digite algo válido!\n")
    continue