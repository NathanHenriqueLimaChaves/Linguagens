print("Bem vindo(a)!\n")
while True:
  try:
    user = input("Digite o nome do usuário: ")
    if(user == ''):
      print("Valor inválido!")
      continue
    else:
      senha = input("Digite uma senha: ")
      if(senha == ''):
         print("Valor inválido!")
         continue
      else:
        if(user == senha):
          print("Seu nome de usuário e sua senha não podem ser iguais!")
          continue
        else:
          print("Bem vindo(a) {user}!")
          break
  except ValueError:
    print("Por favor, digite algo válido.")