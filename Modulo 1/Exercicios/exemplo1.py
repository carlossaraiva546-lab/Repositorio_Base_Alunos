nome = input("Digite seu nome: ")

nota1 =  int(input("insira nota do aluno"))
nota2 = int(input("insira nota do aluno"))
nota3 =  int(input("insira nota do aluno"))
nota4 = int(input("insira nota do aluno"))

media = (nota1 + nota2 + nota3 + nota4) /4
print(media)

arquivo = open("medias.txt","a")
arquivo.write(nome + " | " + str(media) + "\n")
arquivo.close()