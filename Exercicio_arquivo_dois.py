def contarNotas(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

def fazerMedia(arquivo_nomes, arquivo_notas):
    arquivo_nome = open(arquivo_nomes)
    arquivo_nota = open(arquivo_notas)
    arquivo_media = open('notas.txt', 'w')
    nomes = []

    cont = 0
    for text in arquivo_nome:
        nomes.append(text)
    for i in arquivo_nota:
        soma = 0
        media = 0
        soma_string = ""
        soma_lista = []
        soma_string = i
        soma_lista = soma_string.split()
        for j in range(contarNotas(soma_lista)):
            soma += float(soma_lista[j])
        soma /= contarNotas(soma_lista)
        arquivo_media.write(nomes[cont] + " " + str(soma) + " ")
        cont +=1

fazerMedia('oii.txt', 'oi.txt')

