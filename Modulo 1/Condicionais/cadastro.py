

lista = []
while True:

    cadastro = int(input("[1]cadastro\n[2]lista\n[3]excluir pessoa\n[0]encerra o programa"))

    if cadastro == 1:
        menu = input("insira um nome:")
        lista.append(lista)

    elif cadastro == 2:
     print(lista)

    elif cadastro == 3:
     remover = input("")
     lista.remove(remover)

    elif cadastro == 0:
        break
    