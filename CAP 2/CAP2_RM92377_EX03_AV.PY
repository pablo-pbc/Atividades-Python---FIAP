# DEFININDO QUAL O DIA DA SEMANA QUE HAVERÃO AS LIVES DA FIAP

# Definindo os valores iniciais de cada variável
quantidade_votos = 0
segunda  = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0

# Fornecendo as informações e valores iniciais
nome_turma = input("Digite o nome da turma: ")
quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))

# Computando a votação dos dias da semana
while quantidade_votos < quantidade_alunos:

    quantidade_votos = quantidade_votos + 1
    dia_da_semana = int(input("Digite o dia da semana desejado, sendo: 1 - Segunda, 2 - Terça, 3 - Quarta, 4 - Quinta, 5 - Sexta: "))

    #Verificando se a opção correta foi selecionada
    if dia_da_semana == 1 or dia_da_semana == 2 or dia_da_semana == 3 or dia_da_semana == 4 or dia_da_semana == 5:

        #somando o numero de votos para a opção 1 - segunda-feira
        if dia_da_semana == 1:
            segunda = segunda + 1

        #somando o numero de votos para opção 2 - terça-feira
        elif dia_da_semana == 2:
            terca = terca + 1

        #somando o numero de votos para opção 3 - quarta-feira
        elif dia_da_semana == 3:
            quarta = quarta + 1

        # somando o numero de votos para opção 4 - quinta-feira
        elif dia_da_semana == 4:
            quinta = quinta + 1

        # somando o numero de votos para opção 5 - sexta-feira
        elif dia_da_semana == 5:
            sexta = sexta + 1

    #Caso a opção esteja errada, a votação é reiniciada a partir do ultimo voto
    else:
        print("Favor escolher entre as opções 1, 2, 3, 4 OU 5!!")
        print("")
        quantidade_votos = quantidade_votos - 1

#Finalizando a cotagem dos votos e informando o resultado
if quantidade_votos == quantidade_alunos:

    #Considerando que segunda-feira(1) tenha obtido o maior numero de votos.
    if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
        print("A segunda-feira (1) recebeu a maior votação, sendo igual à {}. Portanto, as lives serão de segunda-feira!".format(segunda))
        print("")
        print("Terça, quarta, quinta e sexta-feiras receberam, respectivamento {}, {}, {}, {} votos.".format(terca,quarta,quinta,sexta))

    # Considerando que terça-feira(2) tenha obtido o maior numero de votos.
    elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
        print("A terça-feira (2) recebeu a maior votação, sendo igual à {}. Portanto, as lives serão de terça-feira!".format(terca))
        print("")
        print("Segunda, quarta, quinta e sexta-feiras receberam, respectivamento {}, {}, {}, {} votos.".format(segunda,quarta,quinta,sexta))

    # Considerando que quarta-feira(3) tenha obtido o maior numero de votos.
    elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
        print("A quarta-feira (3) recebeu a maior votação, sendo igual à {}. Portanto, as lives serão de quarta-feira!".format(quarta))
        print("")
        print("Segunda, terça, quinta e sexta-feiras receberam, respectivamento {}, {}, {}, {} votos.".format(segunda,terca,quinta,sexta))

    # Considerando que quinta-feira(4) tenha obtido o maior numero de votos.
    elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
        print("A quinta-feira (4) recebeu a maior votação, sendo igual à {}. Portanto, as lives serão de quinta-feira!".format(quinta))
        print("")
        print("Segunda, terça, quarta e sexta-feiras receberam, respectivamento {}, {}, {}, {} votos.".format(segunda,terca,quarta,sexta))

    # Considerando que sexta-feira(5) tenha obtido o maior numero de votos.
    elif sexta > segunda and sexta > terca and sexta > quinta and sexta > quarta:
        print("A sexta-feira (5) recebeu a maior votação, sendo igual à {}. Portanto, as lives serão de sexta-feira!".format(sexta))
        print("")
        print("Segunda, terça, quarta e quinta-feiras receberam, respectivamento {}, {}, {}, {} votos.".format(segunda,terca,quarta,quinta))

    #Caso haja empate, os votos serão mostrados e a votação deverá ser reiniciada.
    elif segunda == terca or segunda == quarta or segunda == quinta or segunda == sexta or terca == quarta or terca == quinta or terca == sexta or quarta == quinta or quarta == sexta or quinta == sexta:
        print("")
        print("Houve empate, veja os votos abaixo e reinicei a votação !")
        print("")
        print("Segunda-feira teve {} votos!".format(segunda))
        print("Terça-feira teve {} votos!".format(terca))
        print("Quarta-feira teve {} votos!".format(quarta))
        print("Quinta-feira teve {} votos!".format(quinta))
        print("Sexta-feira teve {} votos!".format(sexta))

