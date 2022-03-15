#VERIFICANDO A FAIXA DOS BATIMENTOS CARDIACOS POR MINUTO DE ACORDO COM A IDADE

#Inputando as variaveis fornecidas pelo usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
BPM = float(input("Digite seus batimentos por minuto (BPM): "))

#Idade até 7 anos
if idade <= 7 and (BPM >= 120 and BPM <= 140):
    print('{} seu Baticamento cardíaco por minuto está dentro da faixa adequada!'.format(nome))
elif idade <= 7 and BPM > 140:
    print('{} seu Batimento Cardíaco por Minuto está acima da faixa adequada'.format(nome))
elif idade <= 7 and BPM < 120:
    print('{} seu Batimento Cardíaco por Minuto está abaixo da faixa adequada'.format(nome))

#Idade de 8 a 17 anos
elif (idade >= 8 and idade <= 17) and (BPM >= 80 and BPM <= 100):
    print('{} seu Baticamento cardíaco por minuto está dentro da faixa adequada!'.format(nome))
elif (idade >= 8 and idade <= 17) and BPM > 80:
    print('{} seu Batimento Cardíaco por Minuto está acima da faixa adequada'.format(nome))
elif (idade >= 8 and idade <= 17) and BPM < 100:
    print('{} seu Batimento Cardíaco por Minuto está abaixo da faixa adequada'.format(nome))

#Idade de 18 a 65 anos
elif (idade >= 18 and idade <= 65) and (BPM >= 70 and BPM <= 80):
    print('{} seu Baticamento cardíaco por minuto está dentro da faixa adequada!'.format(nome))
elif (idade >= 18 and idade <= 65) and BPM > 70:
    print('{} seu Batimento Cardíaco por Minuto está acima da faixa adequada'.format(nome))
elif (idade >= 18 and idade <= 65) and BPM < 80:
    print('{} seu Batimento Cardíaco por Minuto está abaixo da faixa adequada'.format(nome))

# Idade a partir de 65 anos
elif idade > 65 and (BPM >= 50 and BPM <= 60):
    print('{} seu Baticamento cardíaco por minuto está dentro da faixa adequada!'.format(nome))
elif idade > 65 and BPM > 50:
    print('{} seu Batimento Cardíaco por Minuto está acima da faixa adequada'.format(nome))
elif idade > 65 and BPM < 60:
    print('{} seu Batimento Cardíaco por Minuto está abaixo da faixa adequada'.format(nome))