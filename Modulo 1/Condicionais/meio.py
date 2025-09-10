

    nome = input("insira o seu nome: ")
    peso = float(input("insira seu peso: "))
    altura = float(input("insira sua altura: "))



    imc = peso / (altura**2)

    if imc >= 18.5:
        print("abaixo do peso")
    elif imc < 24.9:
        print("peso normal")
    elif imc < 29.9:
        print("sobrepeso")
    elif imc < 34.9:
        print("obesiade grau I")
    elif imc < 39.9:
        print("obesidade grau II")
    else:
        print("obesideda grau III")
