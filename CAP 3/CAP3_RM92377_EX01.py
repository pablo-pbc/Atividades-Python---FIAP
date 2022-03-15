#Programa de controle de calorias ingeridas por dia. 

#Variavel do tipo lista, que seja preenchida pelo usuário
lista_alimentos = []
lista_calorias = []

indice_listas = -1 #Variavel para mostrar o alimento na posição
soma_colarias = 0 #Variavel para somar as calorias informadas pelo usuário

print('-'*30) #Perfumaria
print('CALORIA INGERIDA POR DIA!')#Título do programa
print('-'*30)

print('')#Pulando de linha
quantidade_alimentos = int(input('Digite a quantidade de alimentos ingeridos hoje: ')) #Variavel digitada pelo usuário indicando a quantidade de alimentos ingeridos no dia atual.
print('')

#Estrutura de repetição para criação da lista de alimentos. O que define a quantidade de repetição é a variavel "quantidade_alimentos" informada pelo usuário
for x in range (quantidade_alimentos):
    alimentos = str(input('Digite o alimento ingerido: ')) #Inclusão do alimento feita pelo usuário

    lista_alimentos.append(alimentos) #Comando "append" para adição de itens na lista (Nesse caso, o item será adicionado no final da lista).

print('')
print(lista_alimentos) #Mostrando a lista de alimentos para o usuário verificar se está correta. 
print('')

#Verificando, através da resposta do usuário, se a lista está correta ou precisa de algum ajuste.
verificacao_lista_alimentos = str (input('A lista de alimentos acima está correta? Sim (S) ou não (N)?: '))

#Caso a lista esteja incorreta 
while verificacao_lista_alimentos.upper() == 'N':
    
    #O usuário informará o tipo de correção que deseja realizar
    correcao = int(input('Qual correção você deseja realizar ? \n 1 = Remoção \n 2 = Acrescentar \n 3 = Substituir \n Resposta: '))
    
    if correcao == 1: #Se a correção selecionada for = 1, então utilizaremos a opção "Remoção"

        indice_listas = -1 #Atualizando o valor do indice_lista para mostrar a posição correta de cada alimento.

        print('*'*20)
        print('LISTA DE ALIMENTOS:') #titulo para listas de alimentos
        print('*'*20)

        for x in lista_alimentos: #Criando amostragem da lista para o usuário ver como está a lista que está criando.

            indice_listas += 1 #Incrementando o valor do indice_listas, para mostrar a posição do alimento para o usuário.
            print( int(indice_listas),' - ', str(x)) #'X' está assumindo o valor de cada item da lista, e repetindo o processo até o término da lista.

        print('')
        remocao = int (input('Em qual posição está o alimento que deseja remover ? \n Resposta: ')) #Verificando a posição do item que deverá ser removido da lista
        print('')

        lista_alimentos.pop(remocao) #Comando .pop() para remover o item de uma posição específica. A variavel "remocao" indica a posição.

        indice_listas = -1

        print('*'*20)
        print('LISTA DE ALIMENTOS:') #titulo para listas de alimentos
        print('*'*20)
        
        for x in lista_alimentos:

            indice_listas += 1
            print( int(indice_listas),' - ', str(x))
        
        print('')

    elif correcao == 2: #Se a correção selecionada for = 2 então utilizaremos a opção "Acrescentar"
        indice_listas = -1

        print('*'*20)
        print('LISTA DE ALIMENTOS:')
        print('*'*20)

        for x in lista_alimentos:

            indice_listas += 1
            print( int(indice_listas),' - ', str(x))

        print('')
        qtd_alimentos_acrescentar = int (input('Quantos alimentos deseja acrescentar ? \n Resposta: '))# Verificando se o usuário deseja acrescentar mais de 1 alimentos na lista. 
        print('')
        indice_listas = -1

        for x in range (qtd_alimentos_acrescentar): #Estrutura de repeticação baseada na quantidade de alimentos informadas pelo usuário.
            
            acrescentar = str (input('Qual o alimento deseja acrescentar ? \n Resposta: ')) #Acrescentando os alimentos
            print('')
            lista_alimentos.append(acrescentar) #Comando .append() para acrescentar os alimentos no final da lista.
        
        print('*'*20)
        print('LISTA DE ALIMENTOS:')
        print('*'*20)

        for x in lista_alimentos:

            indice_listas += 1
            print( int(indice_listas),' - ', str(x))
        
        print('')
    
    elif correcao == 3: #Se a correção selecionada for = 3, então utilizaremos a opção de substituição.
        indice_listas = -1

        print('*'*20)
        print('LISTA DE ALIMENTOS:')
        print('*'*20)

        for x in lista_alimentos:

            indice_listas += 1
            print( int(indice_listas),' - ', str(x))

        print('')
        substituicao = int (input('Qual a posição do alimento que deseja substituir? \n Resposta: ')) #Verificando qual o item que o usuário deseja substituir
        print('')
        lista_alimentos.pop(substituicao) #Comando .pop() para remover o item selecionado. Seleção informada pela variavel "Subtituição" indicada pelo usuário.

        print('')
        reposicao = str (input('Qual o novo alimento? \n Resposta: ')) #Colocando o novo item na lista. A variavel "reposicao" assumirá o valor digitado pelo usuário.
        print('')
        lista_alimentos.insert(substituicao,str(reposicao))

        indice_listas  = -1

        print('*'*20)
        print('LISTA DE ALIMENTOS:')
        print('*'*20)

        for x in lista_alimentos:

            indice_listas += 1
            print( int(indice_listas),' - ', str(x))
        
    print('')
    verificacao_lista_alimentos = str (input('A lista de alimentos acima está correta ? Sim (S) ou Não (N) ? \n Resposta: '))
    print('')


if verificacao_lista_alimentos.upper() == 'S': #Caso a lista esteja correta, o usuario informará as calorias de cada alimento
    indice_listas = -1

    tamanho_lista = len(lista_alimentos)

    #Estrutura de repetição para criação da lista de calorias por alimento. O que define a quantidade de repetição é a variavel "quantidade_alimentos" informada pelo usuário
    for x in range (tamanho_lista):

        indice_listas += 1 #Incremento do índice para mostrar o alimento seguinte

        #Inclusão de calorias por alimento, feita pelo usuário
        calorias = float(input('Digite a coloria do seguinte alimento: {} - '.format(lista_alimentos[indice_listas]))) #"indice_alimento" é a variavel que mostra o alimento na posição "x" da lista - [x , x]

        lista_calorias.append(calorias) #Comando "append" para adição de itens na lista (Nesse caso, o item será adicionado no final da lista).

    indice_listas = -1
    print('*'*20)
    print('CALORIAS POR ALIMENTO:')
    print('*'*20)
   
    for x in lista_calorias: #Amostragem da lista de calorias por alimentos e cada uma das suas posições

        indice_listas += 1
        print(indice_listas, '-', lista_alimentos[indice_listas], ': ', lista_calorias[indice_listas],'kcal') #posição - alimento da lista por posição - calorias por alimentos e por posição
    
    print('')
    verificacao_lista_calorias = str (input('As calorias por alimentos inseridas estão corretas? Sim (S) ou Não (N)? \n Resposta: '))
    print('')

    while verificacao_lista_calorias.upper() == 'N': #Caso a lista de calorias esteja errada

        indice_listas = -1
        print('*'*20)
        print('CALORIAS POR ALIMENTO:') #Título lista de calorias
        print('*'*20)

        for x in lista_calorias:
    
            indice_listas += 1
            print(indice_listas, '-> ', lista_alimentos[indice_listas], ': ', lista_calorias[indice_listas],'kcal')

        substituicao = int (input('Qual a posição da caloria que deseja refazer? \n Resposta: '))#Verificando a caloria informada erroneamente
        print('')
        lista_calorias.pop(substituicao) #Removendo a colaria errada

        reposicao = float (input('Qual o valor da nova caloria? \n Resposta: ')) #Variavel "reposição" sendo alimentada pela nova caloria informada pelo usuário
        print('')
        lista_calorias.insert(substituicao,reposicao)#Inserção da nova caloria "reposição" na posição "substituição".
        print('')

        indice_listas = -1
        print('*'*20)
        print('CALORIAS POR ALIMENTO:') #Título lista de calorias
        print('*'*20)

        for x in lista_calorias:
    
            indice_listas += 1
            print(indice_listas, '-> ', lista_alimentos[indice_listas], ': ', lista_calorias[indice_listas],'kcal')
            print('')

        print('')
        verificacao_lista_calorias = str (input('As calorias por alimentos inseridas estão corretas? Sim (S) ou Não (N)? \n Resposta: '))
        print('')   
    
    if verificacao_lista_calorias.upper() == 'S':
        soma_colarias = sum (lista_calorias)

        print('-'*60)
        print('A quantidade de calorias ingeridas hoje foi de: {} Kcal'.format(soma_colarias))
        print('-'*60)
    

