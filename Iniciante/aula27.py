"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs. a função len retorna a qtd de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[8]) #Pega um valor especifico
print(variavel[-1]) #funciona com negativo, só vai até -1 pois o 0 é utilizado no positivo
print(variavel[4:]) #Pega de determinado valor até o fim
print(variavel[4:]) #Pega do início até determinado valor
print(variavel[4:8]) #Pega de determinado valor até outro especificado
print(variavel[1:5:2]) #Pega do primeiro valor até o ultimo pulando de 2 em dois
print(variavel[::2]) #Pode deixar sem valor também
print(len(variavel)) #Mostra quantos valores possui a variável
