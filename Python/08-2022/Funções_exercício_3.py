'''
3 - Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e 
custo, que é o custo de um item antes do imposto. A função "altera" o valor de custo para
incluir o imposto sobre vendas.
'''
def somaImposto(taxaImposto, custo):
    imposto = float(taxaImposto/100)
    valor = float(custo)
    final = valor+(valor*imposto)
    print(f"O valor final, já incluído o imposto, é de: R${final} reais.")

somaImposto(20,250) 
somaImposto(17.5,300)