"""
    CONSTANTE = "variaveis" que nao vao mudar
    Muitas condicoes no mesmo if(ruim)
    <- Contagem de complexidade(ruim)
"""

velocidade = 60 # velocidade atual do carro 
local_carro = 100 #local em que o carro esta na estrada

# constante nao deve mudar
RADAR_1 = 60 # velocidade maxima do radar 1 
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGER = 1 # A distancia onde o radar pega

velocidade_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 =local_carro >= (LOCAL_1 - RADAR_RANGER) and \
    local_carro <= (LOCAL_1 + RADAR_RANGER)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_pass_radar_1

if velocidade_carro_pass_radar_1:
    print('Velocidade carro passou do radar')

if carro_multado_radar_1:
    print('carro multado em radar 1')