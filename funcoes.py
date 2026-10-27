def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes_novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes_novo_navio)
    else:
        frota[nome_navio] = [posicoes_novo_navio]
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


def posiciona_frota(frota):
    tabuleiro = [[0 for x in range(10)] for x in range(10)]
    for navios in frota.values():
        for posicoes in navios:
            for coordenada in posicoes:
                linha = coordenada[1]
                coluna = coordenada[2]
                tabuleiro[linha][coluna] = 0
                
    return tabuleiro
