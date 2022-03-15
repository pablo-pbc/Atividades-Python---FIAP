
def funcaofibonacci():

    #Numeros inicias da sequencia de Fibonacci
    num_f1 = 0
    num_f2 = 1
    contagem = 0

    #flag
    verif_num = False
    pause_while = False

    #Declaração de variáveis indicadas pelo usuário
    n = int(input('Digite o numero que deseja verificar:' ))

    #Mostrando o inicio da sequencia de fibonacci
    print('') #Pulando linha
    print('{} -> {} '.format(num_f1, num_f2), end = '')
    
    while contagem <= n and pause_while == False:
        
        #Somatória para realização da sequência de fibonacci
        num_f3 = num_f1 + num_f2

        #Continuando a sequencia usuando estrutura de repetição
        print('-> {}'.format(num_f3), end = '')

        #Fazendo com que os numeros "caminhem" para direita ****
        num_f1 = num_f2
        num_f2 = num_f3

        #Verificando se o numero de pesquisa está na sequencia de fibonacci gerada pela somatória e descolamento das variáveis acima.
        if num_f1 == n or num_f2 == n or num_f3 == n:

            verif_num = True #Variavel flag booleana para indicar se o numero está ou não na sequencia.
            pause_while = True #Variavel flag booleana para parar o comando while quando o numero pesquisado aparecer na sequencia.

        #Contador para finalizar o comando while
        contagem += 1

    #Indicando o fim da sequencia de fibonacci de acordo com o numero que deseja verificar
    print('-> FIM')
    print('') #Pulando linha

    #Caso o flag (verif_num) for igual a True (Verdadeiro) indicará que o numero pesquisado faz parte da sequencia de fibonacci
    if verif_num == True:
        print('')
        print('Ação bem sucedida!')
        print('')

    #Caso o flag (verif_num) for igual a False (Falso) indicará que o numero pesquisado não faz parte da sequencia de fibonacci
    else:
        print('')   
        print('Ação não realizada!')
        print('')



    