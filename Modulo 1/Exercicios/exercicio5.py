def somaimposto (taxaimposto,custo):
    return ((custo * taxaimposto) / 100)+ custo


custo = float(input("digite o custo:"))
taxaimposto = float(input("digite a taxa do imposto:"))

print("O valor do seu imposto sobre as vendas:", somaimposto(taxaimposto,custo))

