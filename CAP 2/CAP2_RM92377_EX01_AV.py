#CALCULO PARA INDICE DE MASSA CORPORAL

#Variaveis fornecidas pelo usuário
nome = input("Digite o seu nome: ")
peso = float(input("{} digite o seu peso em Kg: ".format(nome)))
altura = float(input("{} digite a sua altura em metros: ".format(nome)))

#Quebra de linha
print("")

#Calculo do indice de massa corporal
IMC = float(peso / (altura * altura))

#IMC abaixo de 16
if IMC < 16.00:
    print("{} seu índice de massa coporal é {:.2f}, ou seja, Baixo peso Grau III!".format(nome,IMC))

#IMC maior ou igual a 16 e menor que 16.
elif IMC >= 16.00 and IMC <= 16.99:
    print("{} seu índice de massa coporal é {:.2f}, ou seja, Baixo peso Grau II!".format(nome,IMC))

#IMC maior ou igual a 17 e menor que 18.49.
elif IMC >= 17.00 and IMC <= 18.49:
    print("{} seu índice de massa coporal é {:.2f}, ou seja, Baixo peso Grau I!".format(nome,IMC))

#IMC maior ou igual a 18.50 e menor que 24.99.
elif IMC >= 18.50 and IMC <= 24.99:
    print("{} seu índice de massa coporal é {:.2f}, ou seja, Peso ideal!".format(nome,IMC))

#IMC maior ou igual a 25 e menor que 29.99.
elif IMC >= 25.00 and IMC <= 29.99:
    print("{} seu índice de massa coporal é {:.2f}, ou seja, Sobrepeso!".format(nome,IMC))

#IMC maior ou igual a 30 e menor que 34.99.
elif IMC >= 30.00 and IMC <= 34.99:
    print("{} seu índice de massa coporal é {:.2f}, ou seja, Obesidade Grau I!".format(nome,IMC))

#IMC maior ou igual a 35 e menor que 39.99.
elif IMC >= 35.00 and IMC <= 39.99:
    print("{} seu índice de massa coporal é {:.2f}, ou seja, Obesidade Grau II!".format(nome,IMC))

#IMC maior que 40.
elif IMC >= 40.00:
    print("{} seu índice de massa coporal é {:.2f}, ou seja, Obesidade Grau III!".format(nome,IMC))