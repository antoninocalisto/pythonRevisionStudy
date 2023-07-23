def perguntar():
    return input("O que deseja realizar? \n " +
                 "<> - Para inserir um usuário\n " +
                 "<> - Para pesquisar um usuário \n" +
                 "<> - Para excluir um usuario \n" +
                 "<> - Para listar um usuário"
                 ).upper()
def inserir(dicionario):
    dicionario[input("Digite o login:").upper()] = [input("Digite o nome:").upper(),
                                                  input("Data do ultimo acesso:").upper(),
                                                  input("Qual a ultima estacao acessada:").upper()
                                                  ]
    salvar(dicionario)

def salvar(dicionario):
    with open("banco_de_dados_bd.txt", "a") as arquivo:
        for chave,valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))