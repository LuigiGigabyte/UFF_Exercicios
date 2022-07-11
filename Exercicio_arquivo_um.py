import random
def fazerLista(n, nome_arquivo):
    arquivo = open(nome_arquivo, 'w')
    for i in range(n):
        aleatorio_idade = random.randint(1,99)
        arquivo.write(str(nomes[random.randint(0,14)]))
        arquivo.write(" ")
        arquivo.write(str(sobrenomes[random.randint(0,8)]))
        arquivo.write(" ")
        arquivo.write(str(aleatorio_idade))
        arquivo.write( "\n")
    arquivo.close()


nomes = ['Luigi', 'Misa', 'Leo', 'Cris', 'Lucas', 'Linhares', 'Maresias', 'Roger', 'Voltz', 'Xxxtentacion', 'Last', 'synmi', 'kamiya', 'valek']
sobrenomes = ['Silva', 'Junior', 'Silveira', 'Cardoso', 'Ferreira', 'Rocha', 'Santos', 'Almeida', 'Mendes']
num = 0
num = int(input("Informa a quantidade de nomes e idades"))
fazerLista(num, 'oii.txt')