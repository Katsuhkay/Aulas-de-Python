'''
Operadores lógicos
and (e) or (ou) not (não)
and -> Todas as condições precisam ser veridadeiras
or -> apenas uma condição precisa ser verdadeira
not -> O operador not inverte o valor lógico de uma condição. Se a condição for True, not a torna False, e vice-versa.
'''


entrada = input('[E] entar ou [S] sair: ')

entrada = entrada.lower()

senha_permitida = '123'

if entrada == 'e':
    senha_digitada = input('Senha: ')
    if senha_digitada != senha_permitida:
        print('Senha incorreta!')
    else:
        print('Você entrou no sistema!')
elif entrada == 's':
    print('Você saiu do sistema!')
else:
    print('Opção inválida.')

