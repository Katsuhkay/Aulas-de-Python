contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue #Pula o valor 6

    if contador >= 10 and contador <= 28:
        print('Não vou mostrar o ', contador)
        continue

    print(contador)

    if contador == 40:
        break

print('Fim da execução')