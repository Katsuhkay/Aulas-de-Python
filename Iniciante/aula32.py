"""
Faça um programa que peçao ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digitar uma numero inteiro,
informe que eles número não é inteiro
"""

"""
Faça um programa que pergunte a hora ao usuário e, basenado-se nessa hora exiba a saudação apropriada
Bom dia (0-11), Boa tarde(12-17) e Boa noite (18-23)
"""

"""
Faça um programa que peça  o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva que seu nome é curto,
se tiver entre 5 e 6 letras, seu nome é normal, se tiver 7 ou mais seu nome é longo
"""

#Código 1

numero_inteiro = int(input("Digite um número inteiro que irei lhe informar se é positivo ou negativo: "))


if numero_inteiro % 2 == 0:
    print(f"O número {numero_inteiro} é um valor par.")
else:
    print(f"O numero {numero_inteiro} é um valor ímpar")


# Código 2

hora_fornecida = int(input("Olá, bem vindo. Poderia me informar que horas são? "))

if hora_fornecida >= 0 and hora_fornecida <= 11:
    print('Bom dia!')
elif hora_fornecida >= 12 and hora_fornecida <= 17:
    print('Boa tarde!')
elif hora_fornecida >= 18 and hora_fornecida <= 23:
    print('Boa noite!')
else:
    print('Você digitou algo errado! Favor escolher uma hora entre 0 e 23 horas.')

# Código 3

nome = input('Seja bem vindo, poderia informar seu primeiro nome, por favor? ')

if len(nome) <= 4:
    print(f'Bem vindo {nome}, vejo que seu nome é curto, que bom!')
elif len(nome) == 5 or len(nome) == 6:
    print(f'Bem vindo {nome}, vejo que você tem um nome de tamanho normal!')
elif len(nome) >= 7:
    print(f'Bem vindo {nome}, vejo que você tem um nome grande, que legal')