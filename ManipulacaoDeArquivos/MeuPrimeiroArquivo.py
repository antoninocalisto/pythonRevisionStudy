# arquivo = open("primeiro_arquivo.txt", "w")
#
# arquivo.write("Meu primeiro arquivo")
#
# arquivo.close()
# -------------------------------------
# # Append no arquivo
# with open("primeiro_arquivo.txt", "a") as arquivo:
#     arquivo.write("\n Testando arquivo")
# -------------------------------------
# Lendo todas as linhas do arquivo
with open("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)

# -------------------------------------