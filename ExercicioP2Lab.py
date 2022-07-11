agenda = {}

def contarTelefone(nome): #contador para ver quantos números tem tal contato
    contador = 0
    for y in agenda[nome]:
        contador += 1
    return contador

def incluirNovoNome(nome, tel):
    agenda[nome] = tel

def incluirTelefone(nome, tel):
    if (nome in agenda): #caso a pessoa exista na agenda incluirá o telefone dela.
        agenda[nome].append(tel)
    else: #caso a pessoa não exista na agenda pedirá para incluir
        z = 0
        z = int(input("Essa pessoa não existe na agenda. Digite 1 para inclui-lá e 0 para não inclui-lá"))
        if z == 1: #caso queirá incluir, chamará a função incluirNovoNome com os mesmos dados necessários para criar o contato
            incluirNovoNome(nome, tel)

def excluirTelefone(nome, tel):
    if nome in agenda:
        if(contarTelefone(nome) == 1): #caso o nome so tenha um contato excluirá o nome junto, senão, removerá o contato pedido
            agenda.pop(nome)
        else:
            agenda[nome].remove(tel)
    else:
        print("Nome não está na agenda.")

def excluirNome(nome):
    if nome in agenda:
        agenda.pop(nome)
    else:
        print("Nome não está na agenda.")


def consultarTelefone(nome):
    if nome in agenda:
        print(agenda.get(nome))
    else:
        print("Nome não está na agenda.")

contador = 0
opcao = 0
while contador == 0:
    opcao = int(input("Escolha uma das opções\n1 - Incluir novo nome\n2 - Incluir telefone em nome existente\n3 - Excluir telefone de contato existente\n4 - Excluir contato existente\n5 - Consultar o número de telefone de algum contato: "))
    if (opcao == 1):
        nome = input("Insira o nome que quer incluir como contato")
        tel = []
        telefone = 1
        while telefone != "0":
            telefone = input("\nInsira o telefone de contato, digite 0 quando não quiser mais inserir números: ")
            if telefone != "0":
                tel.append(telefone) #faz uma lista de telefones para incluir todos de uma vez
            incluirNovoNome(nome, tel)


    elif opcao == 2:
        nome = input("Insira o nome que quer incluir mais um número de telefone: ")
        telefone = 1
        tel = []
        while telefone != "0":
            telefone = input("\nInsira o telefone de contato, digite 0 quando não quiser mais inserir números: ")
            if telefone != "0":
                tel.append(telefone)
        incluirTelefone(nome, tel)

    elif opcao == 3:
        nome = input("Insira o nome que quer excluir o telefone: ")
        telefone = input("\nInsira o telefone de contato que deseja excluir")
        excluirTelefone(nome, telefone)

    elif opcao == 4:
        nome = input("Insira o nome que quer excluir: ")
        excluirNome(nome)

    elif opcao == 5:
        nome = input("Insira o nome que quer consultar os contatos: ")
        consultarTelefone(nome)
