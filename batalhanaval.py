import random

def main():
    global x, navios_destruidos, navios, mensagem
    mensagem = 'Fim de jogo! Você perdeu!'
    navios_destruidos = 0
    navios = {
        'Porta-Aviões': [5, 'P', 1, 5],
        'Navio de Batalha': [4, 'B', 1, 4],
        'Cruzador': [3, 'C', 1, 3],
        'Destruidor': [2, 'D', 2, 2],
        'Submarino': [1, 'S', 2, 1]
    }

    print("Bem vindo ao programa de BATALHA NAVAL!")
    gerar_tabuleiros()
    while True:
        print("Escolha a sua dificuldade:\n[1] Fácil (50 tentativas)")
        print("[2] Médio (42 tentativas)\n[3] Difícil (35 tentativas)")
        modo = str(input(">>> "))
        match modo:
            case "1":
                x = 50
                print("Você escolheu o modo Fácil")
                break
            case "2":
                x = 42
                print("Você escolheu o modo Médio")
                break
            case "3":
                x = 35
                print("Você escolheu o modo Difícil")
                break
            case _:
                print("Erro! Digite apenas 1, 2 ou 3!")
                continue
    return(jogo(x, navios_destruidos, navios, mensagem))

def jogo(x, navios_destruidos, navios, mensagem):
    while x != 0:
        exibir_tabuleiro()
        casa = selecao_casa()
        if tabuleiro_oculto[casa[0]][casa[1]-1] != '~':
            tabuleiro[casa[0]][casa[1]] = f' {str(tabuleiro_oculto[casa[0]][casa[1]-1])} '
            for navio, infos in navios.items():
                if infos[1] == str(tabuleiro_oculto[casa[0]][casa[1]-1]):
                    infos[0] -= 1
                    if infos[0] == 0:
                        print(f"Você destruiu um {navio}!")
                        navios_destruidos += 1
                        if infos[2] == 2:
                            infos[2] = 1
                            if navio == 'Destruidor':
                                infos[0] = 2
                            else:
                                infos[0] = 1
                    else:
                        print(f"Você acertou um {navio}! ({infos[3]} espaços)")
        else:
            print("Água!")
            tabuleiro[casa[0]][casa[1]] = ' X '
        x -= 1
        print(f"Restam {x} tentativas!")
        print(f"Total de navios destruídos: {navios_destruidos}/7")
        if navios_destruidos == 7:
            mensagem = 'Vitória! Você ganhou!'
            break
    print(f"{mensagem}\nDeseja iniciar um novo jogo? (S/N)")
    while True:
        gameover = str(input(">>> "))
        if gameover.upper().strip() == 'S':
            main()
        elif gameover.upper().strip() == 'N':
            break
        else:
            continue

def gerar_tabuleiros():
    global tabuleiro, tabuleiro_oculto
    tabuleiro = [[ (f'{i+1}  ' if j == 0 else ' ~ ') for j in range(11)] for i in range(10)]
    tabuleiro[9][0] = tabuleiro[9][0].replace('10  ', '10 ')
    tabuleiro_oculto = [['~' for j in range(10)] for i in range(10)]
    for navio, infos in navios.items():
        for e in range(infos[2]):
            posicionado = False
            while not posicionado:
                orientacao = random.choice(['h', 'v'])
                if orientacao == 'h':
                    linha = random.randint(0, 9)
                    coluna = random.randint(0, 10-infos[0])
                    if all(tabuleiro_oculto[linha][coluna+i] == '~' for i in range(infos[0])):
                        for i in range(infos[0]):
                            tabuleiro_oculto[linha][coluna+i] = infos[1]
                        posicionado = True
                    else:
                        posicionado = False
                else:
                    linha = random.randint(0, 10-infos[0])
                    coluna = random.randint(0, 9)
                    if all(tabuleiro_oculto[linha+i][coluna] == '~' for i in range(infos[0])):
                        for i in range(infos[0]):
                            tabuleiro_oculto[linha+i][coluna] = infos[1]
                        posicionado = True
                    else:
                        posicionado = False
    #hack
    #for e in tabuleiro_oculto:
        #print(' '.join(e))

def exibir_tabuleiro():
    print("   ", end="")
    for e in range(ord('A'), ord('A') + 10):
        print(f" {chr(e)} ", end="")
    print()
    for e in tabuleiro:
        print(''.join(e))

def selecao_casa():
    casa = str(input(">>> "))
    casa = list(casa)
    if len(casa) != 2:
        if len(casa) == 3:
            if casa[0].upper() not in 'ABCDEFGHIJ':
                pass
            elif casa[1] == "1" and casa[2] == "0":
                casa[1] = 10
                del casa[2]
            else:
                print("Erro! Valor inválido!")
                return(selecao_casa())
        else:
            print("Erro! Valor inválido!")
            return(selecao_casa())
    if casa[0].upper() not in 'ABCDEFGHIJ':
        print("Erro! Letra inválida! Digite apenas letras entre A e J.")
    else:
        casa[0] = casa[0].upper()
        try:
            casa[1] = int(casa[1])
            if casa[1] < 1 or casa[1] > 10:
                print("Erro! Número inválido! Digite apenas números entre 1 e 10.")
            else:
                if tabuleiro[casa[1]-1][ord(casa[0]) - ord('@')] == ' ~ ':
                    linha = casa[1]-1
                    coluna = ord(casa[0]) - ord('@')
                    return [linha, coluna]
                else:
                    print("Essa casa já foi escolhida antes!")
        except ValueError:
            print("Erro! Valor inválido!")
    return(selecao_casa())

main()
