from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

nomes = ["porta-aviões", "navio-tanque", "contratorpedeiro", "submarino"]
tamanhos = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]

k = 0
while k < len(nomes):
    nome = nomes[k]
    tamanho = tamanhos[k]
    q = 0
    while q < quantidades[k]:
        posicionado = False
        while not posicionado:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if tamanho > 1:
                escolha = int(input("[1] Vertical [2] Horizontal > "))
                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            else:
                orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                posicionado = True
            else:
                print("Esta posição não está válida!")
        q += 1
    k += 1

print(frota)
