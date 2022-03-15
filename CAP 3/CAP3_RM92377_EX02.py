#CONTROLE DE TRANSAÇÕES FEITAS NO DIA


lista_transaçoes = []
indice_lista = -1
contagem_transacao = 0
contagem_custo_transação = 0
soma_transicao = 0

qtd_transacoes = int(input('Quantas transações foram feitas hoje? \n Resposta: '))
print('')

for x in range (qtd_transacoes):
    contagem_transacao += 1

    custo_transcoes = float (input('Digite o custo da transação numero {}: '.format(contagem_transacao)))
    lista_transaçoes.append(custo_transcoes)   

print('')

for x in range(qtd_transacoes):
    indice_lista += 1
    contagem_custo_transação += 1
    print(indice_lista, '- O valor da transação numero {} foi de: R$'.format(contagem_custo_transação), lista_transaçoes[indice_lista])

print('')
verificacao_lista_transacoes = str (input('Os custos informados acima estão corretos ? Sim (S) ou Não (N)? \nResposta: '))
print ('')

while verificacao_lista_transacoes.upper() == 'N':

    substituicao = int (input('Qual a posição do custo que deseja alterar?\nResposta: '))
    lista_transaçoes.pop(substituicao)
    print('')

    reposicao = float (input('Qual o novo custo da transação {}?\n Resposta: '.format(substituicao)))
    lista_transaçoes.insert(substituicao, reposicao)
    print('')

    indice_lista = -1
    
    for x in lista_transaçoes:
        indice_lista += 1
        contagem_custo_transação += 1
        print(indice_lista, '- O valor da transação numero {} foi de: R$'.format(contagem_custo_transação), lista_transaçoes[indice_lista])

    print('')
    verificacao_lista_transacoes = str (input('Os custos informados acima estão corretos ? Sim (S) ou Não (N)? \nResposta: '))

if verificacao_lista_transacoes.upper() == 'S':    
    print('')
    soma_transicao = sum(lista_transaçoes)

    print('*'*60)
    print('O valor total das transações realizadas hoje foi dê: R${}'.format(soma_transicao))
    print('*'*60)