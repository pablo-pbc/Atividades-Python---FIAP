#INDICANDO O VALOR DE DESCONTO DA VIAGEM DE ACORDO COM A CATEGORIA DE ASSENTOR E QUANTIDADE DE VIAJANTES

#Entrada da variavel principal fornecida pelo usuário
categoria_assentos = int(input("Digite a classe da viagem, sendo: 1-Econômica / 2-Executiva / 3- Primeira Classe: "))

#Descontos para classe Economica por quantidade de viajantes, caso a opção de categoria selecionada esteja correta.
if categoria_assentos == 1 or categoria_assentos == 2 or categoria_assentos == 3:

    #Variaveis fornecidas pelo usuário
    valor_bruto = float(input('Digite o valor total da viagem: '))
    quantidade_viajantes = int(input("Digite a quantidade de viagantes: "))

    # Economica, Executiva ou Primeira classe e 1 viajante
    if (categoria_assentos == 1 or categoria_assentos == 2 or categoria_assentos == 3) and quantidade_viajantes == 1:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 1)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 0%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

    #Economica e 2 viajantes
    elif categoria_assentos == 1 and quantidade_viajantes == 2:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 0.97)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 3%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

    #Economica e 3 viajantes
    elif categoria_assentos == 1 and quantidade_viajantes == 3:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 0.96)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 4%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

    #Economica e 4 ou mais viajantes
    elif categoria_assentos == 1 and quantidade_viajantes >= 4:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 0.95)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 5%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

    #Executiva e 2 viajantes
    elif categoria_assentos == 2 and quantidade_viajantes == 2:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 0.95)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 5%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

    #Executiva e 3 viajantes
    elif categoria_assentos == 2 and quantidade_viajantes == 3:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 0.93)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 7%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

    #Executiva e 4 ou mais viajantes
    elif categoria_assentos == 2 and quantidade_viajantes >= 4:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 0.92)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 8%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

    #Primeira Classe e 2 viajantes
    elif categoria_assentos == 3 and quantidade_viajantes == 2:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 0.9)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 10%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

    #Primeira Classe e 3 viajantes
    elif categoria_assentos == 3 and quantidade_viajantes == 3:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 0.85)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 15%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

    #Primeira Classe e 4 ou mais viajantes
    elif categoria_assentos == 3 and quantidade_viajantes >= 4:
        #Calculos
        valor_bruto_desconto = float(valor_bruto * 0.80)
        custo_medio_viajante = valor_bruto_desconto / quantidade_viajantes
        #Resultados
        print("Desconto por categoria e quantidade de Viajantes aplicado foi de: 20%")
        print("O valor bruto da viagem ficou em: {}".format(valor_bruto))
        print("O valor liquido, com desconto, ficou em: {}".format(valor_bruto_desconto))
        print("O custo médio por viajante é de:{}".format(custo_medio_viajante))

#Caso tenha digitado opções fora do solicitado
else:
    print("Favor digitar uma categoria de assentos válida!")