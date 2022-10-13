print("_____Bem-vindo(a) à calculadora de gorjetas!:)_____\n")
conta = float(input("Qual o total da conta? "))
gorjeta = int(
    input("Qual a porcentagem da gorjeta você gostaria de dar?10, 12 ou 15? "))
dividir = int(input("Quantas pessoas irão dividir a conta?"))
gorjeta_count = (gorjeta/100)/dividir
cada_pessoa = (conta / dividir + conta * gorjeta_count)
final_valor = round(cada_pessoa, 2)
final_valor = str(final_valor).replace('.', ',')
print(f"Cada pessoa deve pagar: R${final_valor} reais.")
