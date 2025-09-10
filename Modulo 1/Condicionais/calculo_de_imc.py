nome = input("Informe seu nome: ")
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / altura**2

if imc < 18.5:
    print(f"Senhor(a)",nome,"seu imc é de",imc,"você está abaixo do peso tudo ok")
elif imc < 24.9:
    print(f"Senhor(a)",nome,"seu imc é de",imc,"você está com peso normal tudo ok")
elif imc < 29.9:
    print(f"Senhor(a)",nome,"seu imc é de",imc,"você está Sobrepeso tudo ok")
elif imc < 34.9:
    print(f"Senhor(a)",nome,"seu imc é de",imc,"Obesidade Grau I melhor ter cuidado com a saúde")
elif imc < 39.9:
    print(f"Senhor(a)",nome,"seu imc é de",imc,"Obesidade Grau II melhor ter cuidado com a saúde")
elif imc > 40.0:
    print(f"Senhor(a)",nome,"seu imc é de",imc,"Obesidade Grau III melhor ter cuidado com a saúde")
