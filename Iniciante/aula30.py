"""
CONSTANTE = "Variaáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 65 # Velocidade atual do carro
local_carro = 101 # Local em que o carro está da estrada

radar_1 = 60 #Velocidade máxima permitida do radar 1
loca1_1 = 100 #Local onde o radar 1 está
radar_range = 1 # A distância onde o radar pega

velocidade_carro_passou_radar1 = velocidade > radar_1
carro_multado_radar1 = local_carro >= (loca1_1 - radar_range) and local_carro <= (loca1_1 + radar_range) and velocidade > radar_1

if velocidade_carro_passou_radar1:
    print('Velocidade carrou passou do radar 1')


if carro_multado_radar1 and velocidade_carro_passou_radar1:
    print('Carro multado')