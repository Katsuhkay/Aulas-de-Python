# Conversão de tipo, coerção
# Type conversion, typecasting, coercion
# É o ato de converter um tipo em outro
# Tipos imutáveis e primitivo: str, int, float, bool

#print('1' + 1) # Se dentro de aspas, mesmo sendo número se torna uma str o que torna impossível, concatenar ou somar com int ou float

print('a' + 'b') # Concatena duas strings, ou seja, junta as duas str

print(int('1'), type(int('1'))) # Converteu de str para int

print(int('1') + 1) # Torna-se possível a soma graças à conversão

print(float('1') + 1) # É possível também com float

print(type(float('1') + 1))

print(str(11) + 'abc') # Transformando um número em str é possível a concatenação com str natural.