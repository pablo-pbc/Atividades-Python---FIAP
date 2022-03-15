print('*********************************')
print('***Enterprise Connection-iFood***')
print('*********************************')

restaurantes = [['O Mineiro', 4.3, 'Brasileira', 1.7, '30-40 min', 'gratis'],
                ['Lamen Kazu - Liberdade', 4.8, 'Japonesa', 0.7, '31-41 min', 'R$ 6.99'],
                ['Amor Aos Pedaços', 4.3, 'Doces e Bolos', 1.2, '46-56 min', 'R$ 5.99'],
                ['Mr. Pritzels', 4.7, 'Lanches', 1.3, '30-40 min', 'R$ 4.99'],
                ['We Coffee', 4.5, 'Cafeteria', 0.5, '45-55 min', 'R$ 4.49'],
                ['Brigadeiro Shopping Paulista', 4.7, 'Doces e Bolos', 1.2, '41-51 min', 'R$ 5.99']]

print('\n')

print('Você gostaria de escolher o restaurante por Nome(1), Nota(2), Distância(3) ou Categoria(4)?')

escolha = int(input('Digite a opção desejada?\n Resposta: '))

print('\n')

if escolha == 1:
    
    nome_ordenado = sorted(restaurantes)

    for nome in nome_ordenado:
        print('Restaurante: {}'.format(nome[0]))
        print('Nota: {}'.format(nome[1]))
        print('Distância: {}'.format(nome[3])),
        print('Categoria: {}'.format(nome[2]))
        print('Preço: {}'.format(nome[5]))
        print('*********************************')

elif escolha == 2:

    nota_ordenada = sorted(restaurantes, reverse=True, key=lambda x: x[1])

    indice1 = 0
    indice2 = 1
    contagem = 0
    
    for nota_ordenata in restaurantes:

        while indice1 < len(nota_ordenada):

            if indice2 == len(nota_ordenada):
                indice2 = 0

            if nota_ordenada[indice1][1] == nota_ordenada[indice2][1] and nota_ordenada[indice1][3] < nota_ordenada[indice2][3]:

                nota_ordenada.append(nota_ordenada[indice1])
                nota_ordenada [indice1] = nota_ordenada[indice2]
                nota_ordenada [indice2] = nota_ordenada.pop()

            if indice2 < len(nota_ordenada):
                indice2 = indice2 + 1
    
            contagem = contagem + 1 

            if contagem == len(nota_ordenada):
                indice1 = indice1 + 1
                contagem = 0

    for nota in nota_ordenada:
        print('Restaurante: {}'.format(nota[0]))
        print('Nota: {}'.format(nota[1]))
        print('Distância: {}'.format(nota[3])),
        print('Categoria: {}'.format(nota[2]))
        print('Preço: {}'.format(nota[5]))
        print('*********************************')

elif escolha == 3:

    distancia_ordenada = sorted(restaurantes, key=lambda x: x[3])

    indice1 = 0
    indice2 = 1
    contagem = 0
    
    for menor_distancia in distancia_ordenada:

        while indice1 < len(distancia_ordenada):

            if indice2 == len(distancia_ordenada):
                indice2 = 0

            if distancia_ordenada[indice1][3] == distancia_ordenada[indice2][3] and distancia_ordenada[indice1][1] > distancia_ordenada[indice2][1]:

                distancia_ordenada.append(distancia_ordenada[indice1])
                distancia_ordenada [indice1] = distancia_ordenada[indice2]
                distancia_ordenada [indice2] = distancia_ordenada.pop()

            if indice2 < len(distancia_ordenada):
                indice2 = indice2 + 1
    
            contagem = contagem + 1 

            if contagem == len(distancia_ordenada):
                indice1 = indice1 + 1
                contagem = 0

    for distancia in distancia_ordenada:
        print('Restaurante: {}'.format(distancia[0]))
        print('Nota: {}'.format(distancia[1]))
        print('Distância: {}'.format(distancia[3])),
        print('Categoria: {}'.format(distancia[2]))
        print('Preço: {}'.format(distancia[5]))
        print('*********************************')

elif escolha == 4:

    categoria_ordenada = sorted(restaurantes, key=lambda x: x[2])

    for categoria in categoria_ordenada:
        print('Restaurante: {}'.format(categoria[0]))
        print('Nota: {}'.format(categoria[1]))
        print('Distância: {}'.format(categoria[3])),
        print('Categoria: {}'.format(categoria[2]))
        print('Preço: {}'.format(categoria[5]))
        print('*********************************')

else:
    print('Opção inválida!')