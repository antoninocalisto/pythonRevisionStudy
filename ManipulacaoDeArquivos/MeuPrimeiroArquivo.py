# arquivo = open("primeiro_arquivo.txt", "w")
#
# arquivo.write("Meu primeiro arquivo")
#
# arquivo.close()

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\n Testando arquivo")