print("Programa para cálculo da população:\n")
while True:
  try:
    populacao_a = float(input("Digite a população inicial 1: ")) 
    populacao_b = float(input("Digite a população inicial 2: "))
    taxa_a = float(input("Qual a taxa de crescimento inicial 1(em %): "))
    taxa_b = float(input("Qual a taxa de crescimento inicial 2(em %): "))
    count = 0
    if(populacao_a < populacao_b):
      print("A população 2 é maior que a população 1!")
      while populacao_a < populacao_b:
        populacao_a = populacao_a + populacao_a*(taxa_a/100)
        populacao_b = populacao_b + populacao_b*(taxa_b/100)
        count += 1
      print(f"Levando em conta as taxas de crescimento 1 e 2 fornecidas, {taxa_a} e {taxa_b}, respectivamente, podemos dizer que as populações vão se igualar em: {count} anos.")
    elif(populacao_a > populacao_b):
      print("A população 1 é maior que a população 2!")
      while populacao_b < populacao_a:
        populacao_a = populacao_a + populacao_a*(taxa_a/100)
        populacao_b = populacao_b + populacao_b*(taxa_b/100)
        count += 1
      print(f"Levando em conta as taxas de crescimento 1 e 2 fornecidas, {taxa_a} e {taxa_b}, respectivamente, podemos dizer que as populações vão se igualar em: {count} anos.")
    elif(populacao_a == populacao_b):
      print("As populações são iguais!")
      while count < 100:
       populacao_a = populacao_a + populacao_a*(taxa_a/100)
       populacao_b = populacao_b + populacao_b*(taxa_b/100)
       count += 1
      round_populacao_a = round(populacao_a)
      round_populacao_b = round(populacao_b)
      print(f"Levando em conta as taxas de crescimento 1 e 2 fornecidas, {taxa_a} e {taxa_b}, respectivamente, podemos dizer que as populações serão, em 100 anos, respectivamente, iguais a:\n{round_populacao_a} habitantes;\n{round_populacao_b} habitantes;")
  except ValueError:
    print("Digite um valor válido!")
