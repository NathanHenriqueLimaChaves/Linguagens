def somaImposto(taxaImposto, custo):
    imposto = float(taxaImposto/100)
    valor = float(custo)
    final = valor+(valor*imposto)
    print(f"O valor final, já incluído o imposto, é de: R${final} reais.")

somaImposto(20,250) 
somaImposto(17.5,300)