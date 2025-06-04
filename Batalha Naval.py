import random

linhas = 10
colunas = 10
numero_embarcacoes = 5

def criar_tabuleiro():
    return [["*" for _ in range(colunas)] for _ in range(linhas)]

def exibir_tabuleiro(tabuleiro):
    print("   " + " ".join([str(i) for i in range(colunas)]))
    for i in range(linhas):
        print(f"{i}  " + " ".join(tabuleiro[i]))

def esta_na_lista(lista, item):
    i = 0
    while i < len(lista):
        if lista[i] == item:
            return True
        i += 1
    return False

def verificar_numero(texto):
    i = 0
    while i < len(texto):
        if texto[i] < '0' or texto[i] > '9':
            return False
        i += 1
    return len(texto) > 0

def ler_coordenadas():
    entrada_valida = False
    linha = -1
    coluna = -1
    while entrada_valida == False:
        string_linha = input(f"Informe a linha (0 a {linhas - 1}): ")
        string_coluna = input(f"Informe a coluna (0 a {colunas - 1}): ")
        
        if verificar_numero(string_linha) and verificar_numero(string_coluna):
            linha = int(string_linha)
            coluna = int(string_coluna)
            if linha >= 0 and linha < linhas and coluna >= 0 and coluna < colunas:
                entrada_valida = True
            else:
                print("Coordenadas fora do tabuleiro.")
                print()
        else:
            print("Entrada inválida. Digite números inteiros.")
            print()
    return linha, coluna

def posicionar_embarcacoes(tabuleiro, embarcacoes, humano=True):
    count = 0
    while count < numero_embarcacoes:
        if humano == True:
            print(f"Posicione a embarcação {count + 1}:")
            linha, coluna = ler_coordenadas()
            if esta_na_lista(embarcacoes, (linha, coluna)) == False:
                embarcacoes.append((linha, coluna))
                count += 1
            else:
                print("Já há uma embarcação nessa posição.")
                print()
        else:
            linha = random.randint(0, linhas - 1)
            coluna = random.randint(0, colunas - 1)
            if esta_na_lista(embarcacoes, (linha, coluna)) == False:
                embarcacoes.append((linha, coluna))
                count += 1

def realizar_ataque(tabuleiro_oculto, tabuleiro_visivel, embarcacoes, jogador=True):
    if jogador == True:
        print("Sua vez de atacar!")
        print()
        linha, coluna = ler_coordenadas()
    else:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        print(f"Computador atacou a posição: ({linha}, {coluna})")
        print()

    if esta_na_lista(embarcacoes, (linha, coluna)):
        print("Acertou uma embarcação!")
        print()
        tabuleiro_visivel[linha][coluna] = "X"
        nova_lista = []
        i = 0
        while i < len(embarcacoes):
            if embarcacoes[i] != (linha, coluna):
                nova_lista.append(embarcacoes[i])
            i += 1
        embarcacoes[:] = nova_lista
    else:
        print("Água!")
        print()
        tabuleiro_visivel[linha][coluna] = "O"

    print(f"Embarcações restantes do adversário: {len(embarcacoes)}")
    print()

def batalha_naval():
    tabuleiro_jogador_oculto = criar_tabuleiro()
    tabuleiro_computador_oculto = criar_tabuleiro()
    tabuleiro_jogador_visivel = criar_tabuleiro()
    tabuleiro_computador_visivel = criar_tabuleiro()

    embarcacoes_jogador = []
    embarcacoes_computador = []

    print("Posicione suas embarcações:")
    print()
    posicionar_embarcacoes(tabuleiro_jogador_oculto, embarcacoes_jogador, humano=True)

    print("Computador posicionando embarcações")
    print()
    posicionar_embarcacoes(tabuleiro_computador_oculto, embarcacoes_computador, humano=False)

    print("\nJogo iniciado!\n")
    print()

    while True:
        print("\nSeu tabuleiro: Ataques visíveis")
        print()
        exibir_tabuleiro(tabuleiro_jogador_visivel)
        print(f"Embarcações restantes do computador: {len(embarcacoes_computador)}")
        print()

        print("\nTabuleiro do computador: Ataques  visíveis")
        print()
        exibir_tabuleiro(tabuleiro_computador_visivel)
        print(f"Suas embarcações restantes: {len(embarcacoes_jogador)}")
        print()

        realizar_ataque(tabuleiro_computador_oculto, tabuleiro_computador_visivel, embarcacoes_computador, jogador=True)
        if len(embarcacoes_computador) == 0:
            print("\nParabéns! Você afundou todas as embarcações do computador!")
            print()
            break

        realizar_ataque(tabuleiro_jogador_oculto, tabuleiro_jogador_visivel, embarcacoes_jogador, jogador=False)
        if len(embarcacoes_jogador) == 0:
            print("\nQue pena! O computador afundou todas as suas embarcações.")
            print()
            break

    print("\nObrigado por jogar!")
    print()
    print("Integrantes da equipe: Emidio, Julio, William")

batalha_naval()