num = 1
lista = []
matriz = []
min_volta = [0, 0, 0, 0, 0, 0, ]
min_tempo = [0, 0, 0, 0, 0, 0, ]
aux = []
aux_dois = 0
aux_tres = 0
media = 0
min_media = 0
min_media_volta = 0
for j in range(6):
    lista = []
    for i in range(11):
        if(i==0):
            lista.append(input(f"Insira o nome do piloto {num}: "))
            num += 1
        else:
            lista.append(float(input(f"Insira a volta de numero {i} do {lista[0]}: ")))
            if(min_tempo[j]==0):
                min_tempo[j]=lista[i]
                min_volta[j]=i
            elif(min_tempo[j]>lista[i]):
                min_tempo[j]=lista[i]
                min_volta[j]=i
    matriz.append(lista)
for x in range(6):
    print(f"O piloto {matriz[x][0]} obteve seu melhor resultado na volta de número {min_volta[x]} com exatamente {min_tempo[x]} segundos\n*********")
for ks in range(6):
    for sk in range(ks+1,6):
        if(min_tempo[ks]>min_tempo[sk]):
            aux_dois = min_tempo[ks]
            min_tempo[ks] = min_tempo[sk]
            min_tempo[sk] = aux_dois
            aux = matriz[ks]
            matriz[ks] = matriz [sk]
            matriz[sk] = aux
            aux_tres = min_volta[ks]
            min_volta[ks] = min_volta[sk]
            min_volta[sk] = aux_tres
print(f"TABELA DE CLASSIFICAÇÃO:\n")
for t in range(6):
    print(f"{t+1}º lugar: {matriz[t][0]} obteve seu melhor resultado na volta de número {min_volta[t]} com exatamente {min_tempo[t]} segundos\n*********")
print(f"Parabéns ao competidor {matriz[0][0]} que obteve o primeiro lugar com exatamente {min_tempo[0]} segundos na {min_volta[0]}º volta")

for c in range(1,11):
    for p in range(6):
        media += matriz[p][c]
    media/=6
    print(f"Média da volta {c} é {media}")
    if(c==1):
        min_media=media
        min_media_volta = c
    elif(min_media>media):
        min_media=media
        min_media_volta = c
    media = 0
print(f"A média de volta mais rápida foi a {min_media_volta} com exatamente {min_media} segundos")


