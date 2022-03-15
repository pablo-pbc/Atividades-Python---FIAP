# CALCULO DE PAGAMENTO REFERENTE AO PLANO MENSAL INSCRITO

# Variaveis iniciais informadas pelo usuário
nome = input("Digite o seu nome: ")
plano = str(input("{} digite o seu plano mensal: ".format(nome)))

# Quebra de linha
print("")

# Verificando se o plano escolhido pelo usuário está correto. Isso independe se o usuário irá digitar em maiusculo ou não.
if plano.upper() == 'BASIC' or plano.upper() == 'SILVER' or plano.upper() == 'GOLD' or plano.upper() == 'PLATINUM':

    faturamento_anual = float(input("{} digite seu faturamento anual: ".format(nome.upper())))

    # Se o plano informado for o BASIC
    if plano.upper() == 'BASIC':
        pagamento = faturamento_anual * 0.3
        print("")
        print("{}, o pagamento que deverá fazer é de: {}".format(nome.upper(),pagamento))

    # Se o plano informado for o SILVER
    elif plano.upper() == 'SILVER':
        pagamento = faturamento_anual * 0.2
        print("")
        print("{}, o pagamento que deverá fazer é de: {}".format(nome.upper(),pagamento))

    # Se o plano informado for o GOLD
    elif plano.upper() == 'GOLD':
        pagamento = faturamento_anual * 0.1
        print("")
        print("{}, o pagamento que deverá fazer é de: {}".format(nome.upper(),pagamento))

    # Se o plano informado for o PLATINUM
    elif plano.upper() == 'PLATINUM':
        pagamento = faturamento_anual * 0.05
        print("")
        print("{}, o pagamento que deverá fazer é de: {}".format(nome.upper(),pagamento))

#Caso o plano não informado não esteja dentro das opções, irá exibir a mensagem abaixo.
else:
    print("Favor digitar um plano válido!")