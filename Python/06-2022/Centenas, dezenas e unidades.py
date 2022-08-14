numero = int(input("Digite um número inteiro: "))
try:
    if(numero >= 1 and numero < 1000):
            if(numero >= 100):
                numero_unidade = round((numero%10))
                numero_etapa1 = numero - numero_unidade
                numero_etapa2 = numero_etapa1/10
                numero_dezena = round((numero_etapa2%10))
                numero_centena1 = (numero - numero_unidade) - (numero_dezena*10)
                numero_centena = round((numero_centena1/100))
                if(numero_dezena > 0 and numero_unidade > 0):
                    if(numero_centena == 1 and numero_dezena == 1 and numero_unidade == 1):
                      print(f"O número {numero} possui: {numero_centena} centena, {numero_dezena} dezena e {numero_unidade} unidade.")
                    elif(numero_centena > 1 and numero_dezena == 1 and numero_unidade == 1):
                      print(f"O número {numero} possui: {numero_centena} centenas, {numero_dezena} dezena e {numero_unidade} unidade.")
                    elif(numero_centena == 1 and numero_dezena > 1 and numero_unidade == 1):
                      print(f"O número {numero} possui: {numero_centena} centena, {numero_dezena} dezenas e {numero_unidade} unidade.")
                    elif(numero_centena == 1 and numero_dezena == 1 and numero_unidade > 1 ):
                      print(f"O número {numero} possui: {numero_centena} centena, {numero_dezena} dezena e {numero_unidade} unidades.")
                    elif(numero_centena > 1 and numero_dezena > 1 and numero_unidade == 1):
                      print(f"O número {numero} possui: {numero_centena} centenas, {numero_dezena} dezenas e {numero_unidade} unidade.")
                    elif(numero_centena > 1 and numero_dezena == 1 and numero_unidade > 1):
                      print(f"O número {numero} possui: {numero_centena} centenas, {numero_dezena} dezena e {numero_unidade} unidades.")
                    elif(numero_centena == 1 and numero_dezena > 1 and numero_unidade > 1):
                      print(f"O número {numero} possui: {numero_centena} centena, {numero_dezena} dezenas e {numero_unidade} unidades.")
                    elif(numero_centena > 1 and numero_dezena > 1 and numero_unidade > 1):
                      print(f"O número {numero} possui: {numero_centena} centenas, {numero_dezena} dezenas e {numero_unidade} unidades.")
                elif(numero_dezena == 0 or numero_unidade == 0):
                    if(numero_centena == 1 and numero_dezena == 0 and numero_unidade == 1):
                        print(f"O número {numero} possui: {numero_centena} centena, {numero_dezena} dezena e {numero_unidade} unidade.")
                    elif(numero_centena == 1 and numero_dezena == 1 and numero_unidade == 0):
                        print(f"O número {numero} possui: {numero_centena} centena, {numero_dezena} dezena e {numero_unidade} unidade.")
                    elif(numero_centena == 1 and numero_dezena == 0 and numero_unidade == 0):
                        print(f"O número {numero} possui: {numero_centena} centena, {numero_dezena} dezena e {numero_unidade} unidade.")
                    elif(numero_centena == 1 and numero_dezena > 0 and numero_unidade == 0):
                        print(f"O número {numero} possui: {numero_centena} centena, {numero_dezena} dezenas e {numero_unidade} unidade.")
                    elif(numero_centena == 1 and numero_dezena == 0 and numero_unidade > 0):
                        print(f"O número {numero} possui: {numero_centena} centena, {numero_dezena} dezena e {numero_unidade} unidades.")
                    elif(numero_centena > 1 and numero_dezena == 0 and numero_unidade == 1):
                        print(f"O número {numero} possui: {numero_centena} centenas, {numero_dezena} dezena e {numero_unidade} unidade.")
                    elif(numero_centena > 1 and numero_dezena == 1 and numero_unidade == 0):
                        print(f"O número {numero} possui: {numero_centena} centenas, {numero_dezena} dezena e {numero_unidade} unidade.")
                    elif(numero_centena > 1 and numero_dezena == 0 and numero_unidade == 0):
                        print(f"O número {numero} possui: {numero_centena} centenas, {numero_dezena} dezena e {numero_unidade} unidade.")
                    elif(numero_centena > 1 and numero_dezena > 1 and numero_unidade == 0):
                        print(f"O número {numero} possui: {numero_centena} centenas, {numero_dezena} dezenas e {numero_unidade} unidade.")
                    elif(numero_centena > 1 and numero_dezena == 0 and numero_unidade > 1):
                        print(f"O número {numero} possui: {numero_centena} centenas, {numero_dezena} dezena e {numero_unidade} unidades.")
            elif(numero >= 10 and numero < 100):
                numero_unidade = round((numero%10))
                numero_etapa1 = numero - numero_unidade
                numero_etapa2 = numero_etapa1/10
                numero_dezena = round((numero_etapa2%10))
                if(numero_dezena == 1 and numero_unidade == 0):
                    print(f"O número {numero} possui: {numero_dezena} dezena e {numero_unidade} unidade.")
                elif(numero_dezena == 1 and numero_unidade == 1):
                    print(f"O número {numero} possui: {numero_dezena} dezena e {numero_unidade} unidade.")
                elif(numero_dezena > 1 and numero_unidade == 0):
                    print(f"O número {numero} possui: {numero_dezena} dezenas e {numero_unidade} unidade.")
                elif(numero_dezena > 1 and numero_unidade == 1):
                    print(f"O número {numero} possui: {numero_dezena} dezenas e {numero_unidade} unidade.")
                elif(numero_dezena == 1 and numero_unidade > 1):
                    print(f"O número {numero} possui: {numero_dezena} dezena e {numero_unidade} unidades.")
                elif(numero_dezena > 1 and numero_unidade > 1):
                    print(f"O número {numero} possui: {numero_dezena} dezenas e {numero_unidade} unidades.")
            elif(numero >= 1 and numero < 10):
                numero_unidade = round((numero%10))
                if(numero_unidade == 1):
                    print(f"O número {numero} possui: {numero_unidade} unidade.")
                elif(numero_unidade > 1):
                    print(f"O número {numero} possui: {numero_unidade} unidades.")
    else:
        print("Número fora do intervalo esperado. Tente novamente!")
except ValueError:
    print("Você digitou algo que não é um número inteiro. Tente novamente!")


    
