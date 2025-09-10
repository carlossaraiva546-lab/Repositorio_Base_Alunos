valor_original = int(input("Digite o valor original: "))
porcentagem_desconto = int(input("digite o valor da porcentagem"))


valor_desconto = valor_original*(porcentagem_desconto/100)
preco_final = valor_original - valor_desconto
print(preco_final)