from xml.dom import INDEX_SIZE_ERR


print("Complete com os seus dados, por favor:\n")
def clear():
  print("\n"*40)
num = 1
usuarios_final = []
lista_codigo = []
lista_altura = []
lista_peso = []
while True:
  try:
    
    while num != 0:
      codigo = int(input("Qual o seu código? "))
      if(codigo == 0):
        break
      usuarios = []
      usuarios.append(codigo)
      altura = float(input("Qual a sua altura(m)? "))
      usuarios.append(altura)
      peso = float(input("Qual o seu peso(kg)? "))
      usuarios.append(peso)
      print(f"Usuário_{num}: código {codigo}; Altura(m)-{altura}; Peso(kg)-{peso};")
      num += 1
      usuarios_final.append(usuarios)
      lista_codigo.append(codigo)
      lista_altura.append(altura)
      lista_peso.append(peso)
      print("---------------------------")
    clear()
    print(f"Lista de usuários(C,A e P): {usuarios_final}")
    print(f"Maior altura(m): {max(lista_altura)}")
    print(f"Menor altura(m): {min(lista_altura)}")
    print(f"Maior peso(kg): {max(lista_peso)}")
    print(f"Menor peso(kg): {min(lista_peso)}")
    media_alturas = sum(lista_altura)/(len(lista_codigo))
    print(f"A média das alturas dos clientes é igual a {media_alturas}.")
    media_peso = sum(lista_peso)/(len(lista_codigo))
    print(f"A média dos pesos dos clientes é igual a {media_peso}")
    break
  except ValueError:
    print("Você digitou algo errado. Tente novamente!\n")

 