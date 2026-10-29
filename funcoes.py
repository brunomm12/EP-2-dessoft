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
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
        
    for navios in frota.values():
        for posicoes in navios:
            for coordenada in posicoes:
                linha_navio = coordenada[0]
                coluna_navio = coordenada[1]
                tabuleiro[linha_navio][coluna_navio] = 1
                
    return tabuleiro

def afundados(frota, tabuleiro):
    quantidade_afundados = 0
    for navios_do_tipo in frota.values():
        for navio in navios_do_tipo:
            afundado = True
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            if afundado:
                quantidade_afundados += 1
                
    return quantidade_afundados

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao = "vertical":
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for pos in posicoes:
        if pos[0] < 1 or pos[0] > 9 or pos[1] < 1 or pos[1] > 9:
            return False
        for tipo in frota:
            for navio in frota[tipo]:
                
            for ocupada in navio:
                if ocupada = pos:
                        return False
    return True
