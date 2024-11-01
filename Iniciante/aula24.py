'''
Operadores 'in' e 'not in'
Strings são iteráveis
0 1 2 3 4 5 6 7 8
A L E X R E N A N 
-9 -8 -7 -6 -5 -4 -3 -2 -1
'''

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

# print(nome[0]) # Consultando pelo índice
# print(nome[-10]) # Espaço conta, fica esperto!

# print('x' in nome) # Verifica se contém a letra na variável
# print('z' not in nome) # Verifica se a letra NÃO está na variável

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')