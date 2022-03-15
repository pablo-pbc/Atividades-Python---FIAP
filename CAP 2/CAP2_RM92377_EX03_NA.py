#DEFININDO QUAL O PREMIO DA EQUIPE SORTEADA POR VOTAÇÃO
quantidade_votos = 0
Playstation  = 0
Xbox = 0
Nitendo = 0
#Computando a votação do console indicada pelos membros da equipe
while quantidade_votos < 5:

    quantidade_votos = quantidade_votos + 1
    console_escolhido = int (input("Digite o console desejado, sendo: 1 - Playstation, 2 - Xbox e 3 - Nitendo: "))

    #Verificando se a opção correta foi selecionada
    if console_escolhido == 1 or console_escolhido == 2 or console_escolhido ==3:

        #somando o numero de votos para a opção 1
        if console_escolhido == 1:
            Playstation = Playstation + 1

        #somando o numero de votos para opção 2
        elif console_escolhido == 2:
            Xbox = Xbox + 1

        #somando o numero de votos para opção 3
        elif console_escolhido == 3:
            Nitendo = Nitendo + 1

    #Caso a opção esteja errada, a votação é reiniciada a partir do ultimo voto
    else:
        print("Favor escolher entre as opções 1, 2 ou 3!!")
        quantidade_votos = quantidade_votos - 1

#Finalizando a cotagem dos votos e informando o resultado
if quantidade_votos == 5:

    #Considerando que o Playstation tenha obtido o maior numero de votos.
    if Playstation > Xbox and Playstation > Nitendo:
        print("O Playstation recebeu a maior votação, sendo igual à {}".format(Playstation))
        print("")
        print("O Xbox e o Nintendo tiveram, respectivamento {} e {} votos.".format(Xbox,Nitendo))

    # Considerando que o Xbox tenha obtido o maior numero de votos.
    elif Xbox > Playstation and Xbox > Nitendo:
        print("O Xbox recebeu a maior votação, sendo igual à {}".format(Xbox))
        print("")
        print("O Playstation e o Nintendo tiveram, respectivamento {} e {} votos.".format(Playstation,Nitendo))

    # Considerando que o Nitendo tenha obtido o maior numero de votos.
    elif Nitendo > Playstation and Nitendo > Xbox:
        print("O Nitendo recebeu a maior votação, sendo igual à {}".format(Nitendo))
        print("")
        print("O Playstation e o Xbox tiveram, respectivamento {} e {} votos.".format(Playstation,Xbox))

    #Considerando empate entre Plastation e Xbox
    elif Playstation == Xbox:
        print("Houve empate entre Plastation e Xbox, reiniciar votação e escolher votar somente nas opções 1 e 2!")

        #Reiniciando as variáveis e reiniciando a votação.
        quantidade_votos = 0
        Playstation = 0
        Xbox = 0

        while quantidade_votos < 5:

            quantidade_votos = quantidade_votos + 1
            console_escolhido = int(
            input("Digite o console desejado, sendo: 1 - Playstation e 2 - Xbox: "))

            # Verificando se a opção correta foi selecionada
            if console_escolhido == 1 or console_escolhido == 2:

                # somando o numero de votos para a opção 1
                if console_escolhido == 1:
                    Playstation = Playstation + 1

                # somando o numero de votos para opção 2
                elif console_escolhido == 2:
                    Xbox = Xbox + 1

            # Caso a opção esteja errada, a votação é reiniciada a partir do ultimo voto
            else:
                print("Favor escolher entre as opções 1 ou 2!")
                quantidade_votos = quantidade_votos - 1

        if quantidade_votos == 5:

            # Considerando que o Playstation tenha obtido o maior numero de votos.
            if Playstation > Xbox:
                print("O Playstation recebeu a maior votação, sendo igual à {}".format(Playstation))
                print("")
                print("O Xbox teve {} votos.".format(Xbox))

            # Considerando que o Xbox tenha obtido o maior numero de votos.
            else:
                print("O Xbox recebeu a maior votação, sendo igual à {}".format(Xbox))
                print("")
                print("O Playstation teve {} votos.".format(Playstation))

    # Considerando empate entre Playstation e Nitendo
    elif Playstation == Nitendo:
        print("Houve empate entre Plastation e Nitendo, reiniciar votação e escolher votar somente nas opções 1 e 3!")

        # Reiniciando as variáveis e reiniciando a votação.
        quantidade_votos = 0
        Playstation = 0
        Nitendo = 0

        while quantidade_votos < 5:

            quantidade_votos = quantidade_votos + 1
            console_escolhido = int(
                input("Digite o console desejado, sendo: 1 - Playstation e 3 - Nitendo: "))

            # Verificando se a opção correta foi selecionada
            if console_escolhido == 1 or console_escolhido == 3:

                # somando o numero de votos para a opção 1
                if console_escolhido == 1:
                    Playstation = Playstation + 1

                # somando o numero de votos para opção 2
                elif console_escolhido == 3:
                    Nitendo = Nitendo + 1

            # Caso a opção esteja errada, a votação é reiniciada a partir do ultimo voto
            else:
                print("Favor escolher entre as opções 1 ou 3!")
                quantidade_votos = quantidade_votos - 1

        if quantidade_votos == 5:

            # Considerando que o Playstation tenha obtido o maior numero de votos.
            if Playstation > Nitendo:
                print("O Playstation recebeu a maior votação, sendo igual à {}".format(Playstation))
                print("")
                print("O Nitendo teve {} votos.".format(Nitendo))

            # Considerando que o Xbox tenha obtido o maior numero de votos.
            else:
                print("O Nitendo recebeu a maior votação, sendo igual à {}".format(Nitendo))
                print("")
                print("O Playstation teve {} votos.".format(Playstation))

    # Considerando empate entre Playstation e Nitendo
    elif Xbox == Nitendo:
        print("Houve empate entre Xbox e Nitendo, reiniciar votação e escolher votar somente nas opções 2 e 3!")

        # Reiniciando as variáveis e reiniciando a votação.
        quantidade_votos = 0
        Xbox = 0
        Nitendo = 0

        while quantidade_votos < 5:

            quantidade_votos = quantidade_votos + 1
            console_escolhido = int(
                input("Digite o console desejado, sendo: 2 - Xbox e 3 - Nitendo: "))

            # Verificando se a opção correta foi selecionada
            if console_escolhido == 2 or console_escolhido == 3:

                # somando o numero de votos para a opção 1
                if console_escolhido == 2:
                    Xbox = Xbox + 1

                # somando o numero de votos para opção 2
                elif console_escolhido == 3:
                    Nitendo = Nitendo + 1

            # Caso a opção esteja errada, a votação é reiniciada a partir do ultimo voto
            else:
                print("Favor escolher entre as opções 2 ou 3!")
                quantidade_votos = quantidade_votos - 1

        if quantidade_votos == 5:

            # Considerando que o Playstation tenha obtido o maior numero de votos.
            if Xbox > Nitendo:
                print("O Xbox recebeu a maior votação, sendo igual à {}".format(Xbox))
                print("")
                print("O Nitendo teve {} votos.".format(Nitendo))

            # Considerando que o Xbox tenha obtido o maior numero de votos.
            else:
                print("O Nitendo recebeu a maior votação, sendo igual à {}".format(Nitendo))
                print("")
                print("O Xbox teve {} votos.".format(Xbox))


