from itertools import count


print("Sistema eleitoral!\n")
total_votos = []
while True:
  try:
    voto = int(input("Seu voto: "))
    while voto != 0:
      voto = int(input("Seu voto: "))
      if(voto == 1 or voto == 2 or voto == 3 or voto == 4 or voto == 5 or voto == 6):
        certeza = (input(f"Seu voto é {voto}. Confirma? S/N  "))
        if(certeza == 's' or certeza == 'S'):
          total_votos.append(voto)
          print("Voto confirmado!")
        elif(certeza == 'n' or certeza == 'N'):
          print("De novo:\n")
      elif(voto < 0 or voto > 6):
        print("Valor inválido. Tente novamente!")
    print(total_votos)
    votos_1 = total_votos.count(1)
    votos_2 = total_votos.count(2)
    votos_3 = total_votos.count(3)
    votos_4 = total_votos.count(4)
    votos_nulo = total_votos.count(5)
    votos_branco = total_votos.count(6)
    len_total_votos = len(total_votos)
    porcentagem_1 = round((votos_1/len_total_votos)*100, 2)
    porcentagem_2 = round((votos_2/len_total_votos)*100, 2)
    porcentagem_3 = round((votos_3/len_total_votos)*100, 2)
    porcentagem_4 = round((votos_4/len_total_votos)*100,2)
    porcentagem_nulo = round((votos_nulo/len_total_votos)*100, 2)
    porcentagem_branco = round((votos_branco/len_total_votos)*100, 2)
    print(f"O candidato 1 teve {votos_1} votos! Porcentagem => {porcentagem_1}%")
    print(f"O candidato 2 teve {votos_2} votos! Porcentagem => {porcentagem_2}%")
    print(f"O candidato 3 teve {votos_3} votos! Porcentagem => {porcentagem_3}%")
    print(f"O candidato 4 teve {votos_4} votos! Porcentagem => {porcentagem_4}%")
    print(f"Votos nulos => {votos_nulo}; Porcentagem => {porcentagem_nulo}%")
    print(f"Votos brancos => {votos_branco}; Porcentagem => {porcentagem_branco}%")
    break
  except ValueError:
    print("Comando inválido. Tente novamente!")