#Descobrindo a senha LIBERDADE+FATORIAL MINUTO ATUAL

#Exemplos fatorial:
#4! = 4 · 3 · 2 · 1 = 24
#5! = 5 · 4 · 3 · 2 · 1 = 120
#6! = 6 · 5 · 4 · 3 · 2 · 1 = 720
#7! = 7· 6 · 5 · 4 · 3 · 2 · 1 = 5040

#Importando a função datetime da função datetime padrão do python
from datetime import datetime

#variáveis para desenvolver o fatorial
contador = 1
resultado = 1

#Atribuindo à variavel "minuto_atual", a data e horario atual
minuto_atual = datetime.now()# -> função datetime que retorna data e horario atual

# print (minuto_atual.minute) - > verificando se o o comando ".minute" funcionava

#Fatorial do minuto por estrutura de repetição
while contador <= minuto_atual.minute:       #Supondo que o minuto seja 4
    resultado *= contador                    # resultado: (1 = 1 * 1) = 1 -> resultado: (1 = 1 * 2) = 2 ->  resultado: (2 = 2 * 3)= 6 -> resultado: (6 = 6 * 4)= 24
    contador +=1                             # contador: 1                   contador: 2                    contador: 3                  contador: 4


print('LIBERDADE{} '.format(resultado)) #Exibindo a senha 