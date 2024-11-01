'''
Operadores lógicos
and (e) or (ou) not (não)
and -> Todas as condições precisam ser veridadeiras
or -> apenas uma condição precisa ser verdadeira
not -> O operador not inverte o valor lógico de uma condição. Se a condição for True, not a torna False, e vice-versa.
'''

# NOT

senha = input('Senha: ')

if senha != '123':
    print('Senha incorreta')

print(not True)
print(not False)
