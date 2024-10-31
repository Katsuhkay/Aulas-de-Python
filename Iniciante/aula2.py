print(12, 34, 1011, sep="-") #Separa os valores com o caractere predefinido nas aspas
print(56, 78, sep="@") #Pode ser usado qualquer valor para a separação
print(9, 10, sep='-') #Pode usar aspas simples ou duplas

# \r \n -> CRLF (carry ad return line feed), usado para quebrar a linha!
print(12, 34, 1011, sep=" ", end='##') #Não quebra a linha e deixa a cerquilha na frente!
print(13, 35, 2022, sep=" ", end='\n##') #Quebra a linha e coloca cerquilha na linha inferior
print(14, 36, 3033, sep=" ", end='\r\n')
