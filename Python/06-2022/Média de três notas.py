print("Sistema de cálculo de médias!\n")
nome = str(input("Nome do aluno(a): "))
materia = str(input("Nome da matéria: "))
try:
  nota1 = float(input("Digite a primiera nota:"))
  nota2 = float(input("Digite a segunda nota: "))
  nota3 = float(input("Digite a terceira nota: "))
  media = (nota1+nota2+nota3)/3
  if(media >= 0 and media <= 10):
    if(media == 10):
      print(f"A média foi de {media}. Aluno(a) aprovado(a) com distinção!")
    elif(media >= 7):
      print(f"A média foi de {media}. Aluno(a) aprovado(a).")
    elif(media < 7):
      print(f"A média foi de {media}. Aluno(a) reprovado(a)")
  else:
    print("Média inválida. Confira se você digitou as notas corretas.")
except ValueError:
  print("Você digitou algo errado! Tente novamente.")
