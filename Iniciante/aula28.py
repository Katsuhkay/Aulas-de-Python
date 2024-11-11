"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        seu nome invertido é {nome invertido}
        se seu nome contem (ou não) espaços
        seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba: "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}") #Print de trás para frente

    if ' ' in nome:
        print(f"Seu nome contem espaços.")
    else:
        print('Seu nome não contem espaços.')

    print(f"Seu nome contem {len(nome)} letras")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")
else:
    print(f"Desculpe, você deixou campos vazios.")