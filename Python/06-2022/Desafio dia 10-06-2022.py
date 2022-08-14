#DESAFIO DO DIA 10/06/2022
#DESENVOLVER UM SISTEMA DE BIOIMPEDÂNCIA
print("Bem vindo(a) ao sistema de cálculo de bioimpedância!\n")
print("Vamos iniciar com o seu cadastro!:)\n")
nome = str(input("Digite o seu nome completo: "))
data_nascimento = str(input("Data de nascimento: "))
cpf = str(input("CPF: "))
sexo = str(input("Sexo: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))
print("\n")
print("Baseado no seu cadastro, temos as seguintes informações:\n")
imc = peso/altura**2
print("Composição corporal:\n")
print("*Peso atual = ",peso)
print("*IMC = ",imc)
if(imc < 18.5):
    print("**Baseado no seu IMC, você está ABAIXO DO PESO. Cuide-se melhor!")
elif(imc >= 18.5 and imc <= 24.9):
    print("**Baseado no seu IMC, você está NO PESO NORMAL. Parabéns!")
elif(imc >= 25 and imc <= 29.9):
    print("**Baseado no seu IMC, você está COM SOBREPESO. Cuidado!")
elif(imc >= 30 and imc <= 34.9):
    print("**Baseado no seu IMC, você está COM OBESIDADE GRAU I. Procure um profissional!")
elif(imc >= 35 and imc <= 39.9):
    print("**Baseado no seu IMC, você está COM OBESIDADE GRAU II. Procure um profissional!")
elif(imc >= 40):
    print("**Baseado no seu IMC, você está COM OBESIDADE GRAU III. Procure um profissional!")
if(sexo == 'masculino' or sexo == 'Masculino'):
    peso_ideal = 61.2328+(altura-1.6002)*53.5433
    print("*Peso Ideal = ",peso_ideal)
elif(sexo == 'feminino' or sexo == 'Feminino'):
    peso_ideal = 53.695+(altura-1.524)*53.5433
    print("*Peso Ideal = ",peso_ideal)
else:
    print("Sexo inválido! Tente novamente")
massa_gorda = (peso-peso_ideal)
print("*Massa Gorda = ",massa_gorda)
percentual_gorda = massa_gorda/peso*100
print("*%Massa Gorda = ",percentual_gorda)
massa_magra = (peso-massa_gorda)
print("*Massa Magra = ",massa_magra)
percentual_magra = 100-percentual_gorda
print("*%Massa Magra = ",percentual_magra)


    

