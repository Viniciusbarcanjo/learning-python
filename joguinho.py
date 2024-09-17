import os

# Definindo o jogador e suas coordenadas iniciais
player = {'x': 0, 'y': 0}

# Função para mover o jogador
def andar(direcao):
    if direcao == 'w':
        player['y'] = max(0, player['y'] - 1)  # Move para cima, não permitindo valores negativos
    elif direcao == 's':
        player['y'] = min(4, player['y'] + 1)  # Move para baixo, não permitindo ultrapassar o limite inferior
    elif direcao == 'd':
        player['x'] = min(9, player['x'] + 1)  # Move para a direita, não permitindo ultrapassar o limite direito
    elif direcao == 'a':
        player['x'] = max(0, player['x'] - 1)  # Move para a esquerda, não permitindo valores negativos
    else:
        print("Direção inválida. Use w, s, d, ou a.")

while True:
    os.system('clear')  # Limpa o terminal (no Windows, use 'cls')

    print("--------------------")
    for y in range(5):
        print()  # Para criar uma nova linha
        for x in range(10):
            if player['x'] == x and player['y'] == y:
                print("🚶‍♂️", end="")
            else:
                print("🟩", end="")
        print()  # Para criar uma nova linha após a linha de jogo
    print("------------------------")

    direcao = input("Proxima direcao (w,s,d,a): ")
    andar(direcao)