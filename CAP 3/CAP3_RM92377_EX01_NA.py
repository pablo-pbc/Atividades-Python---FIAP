# Programa para calcular a média dos alunos numeros pares e impares de uma turma

#Variáveis iniciais para o funcionamento do programa
contagem_par = 0
contagem_impar = 0
soma_par = 0
soma_impar = 0
step_pares = 2
step_impares = 1

#Estrutura de repetição, considerando uma turma de 50 alunos e apenas os numeros pares. Começando de 0 a 50 pulando de 2 em 2. (0,50,2) 0 inicio, 50 fim, 2 step
for x in range (0,50,2):
    print('*'*60)
    print('Professor, vocês está digitando as notas dos alunos pares!!')
    print('*'*60)
    print('')
    notas_pares = float (input('Professor, digete a nota do aluno numero {}!\nResposta: '.format(step_pares))) #Inserção das notas dos alunos pares, informadas pelo usuário

    soma_par = soma_par + notas_pares #As notas estão sendo somadas e armazenadas na variavel soma_par

    contagem_par += 1 #Contagem para somar a quantidade total de alunos
    step_pares += 2 #Variavel tendo somando de 2 em 2 para mostrar o numero do aluno para o professor.

media_par = soma_par / contagem_par #Calculando a media dos alunos numeros pares

#Estrutura de repetição, considerando uma turma de 50 alunos e apenas os numeros impares. Começando de 1 a 50 pulando de 2 em 2. (1,50,2) 1 inicio, 50 fim, 2 step
for x in range (1,50,2):
    print('*'*60)
    print('Professor, vocês está digitando as notas dos alunos impares!!')
    print('*'*60)
    print('')
    notas_impares = float (input('Professor, digete a nota do aluno numero {}!\nResposta: '.format(step_impares))) #Inserção das notas dos alunos impares, informadas pelo usuário

    contagem_impar += 1 #Contagem para somar a quantidade total de alunos 
    step_impares += 2 #Variavel tendo somando de 2 em 2 para mostrar o numero do aluno para o professor.

    soma_impar = soma_impar + notas_impares #As notas estão sendo somadas e armazenadas na variavel soma_impar

media_impar = soma_impar / contagem_impar #Calculando a media dos alunos numeros impares

print('')
print('A media dos alunos de numeros pares foi de: {}!'. format(media_par)) #Mostrando a media das notas dos alunos pares
print('')
print('A media dos alunos de numeros impares foi de: {}!'. format(media_impar)) #Mostrando a media das notas dos alunos impares
print('')



