# Cronometro

# Importando as bibliotecas
from time import sleep
import os

# Limpar a tela
def limpar_tela():
    os.system('cls')

# Variáveis
contador = 0
minutos = 1

# Loop principal (contador)
while True:
    print('*' * 7, 'Cronometro', '*' * 7)
    print(f'       | {contador}', ' |')
    print('-' * 26)
    contador += 1

    # Iniciar a contagem dos minutos
    if contador > 60:
        limpar_tela()
        contador = 0
        # Loop para os minutos
        while True:
            print('*' * 7, 'Cronometro', '*' * 7)
            print(f'       | {minutos}:{contador}', ' |')
            print('-' * 26)
            contador += 1
            # Recomeçar a contagem dos segundos
            if contador > 59:
                contador = 0
                minutos += 1
            sleep(1)
            limpar_tela()
        sleep(1)
        limpar_tela()


