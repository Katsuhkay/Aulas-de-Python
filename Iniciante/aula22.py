'''
Operadores lógicos
and (e) or (ou) not (não)
and -> Todas as condições precisam ser veridadeiras
or -> apenas uma condição precisa ser verdadeira
not -> O operador not inverte o valor lógico de uma condição. Se a condição for True, not a torna False, e vice-versa.
'''


entrada = input('[E] entar ou [S] sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print("Você entrou no sistema!")
else:
    print('Voce saiu dos sistema!')