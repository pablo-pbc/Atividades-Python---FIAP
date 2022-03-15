# EXERCICIO DE VERIFICAÇÃO SE O NUMERO SE ENCONTRA NA SEQUENCIA DE FIBONACCI OU NÃO
# Sequencia de fibonacci: 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21... 
#                       ->f1  f2  f3
#                       ->->->f1  f2  f3
#                       ->->->->->f1  f2  f3
# A ideia é para verificar o numero é fazer as variaveis "caminharem" para direita e assim realizar a sequencia de fibonacci ***

#importando funções 
from CAP3_RM92377_FUNÇOES import funcaofibonacci


# Título
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
print('')

print('')
resposta = str(input('Deseja iniciar a vericação do numero? Sim (S) ou não (N)? '))
print('')

while resposta.upper() != 'N':

    funcaofibonacci()

    print('')
    resposta = str(input('Deseja continuar a vericação do numero? Sim (S) ou não (N)? '))
    print('')








