# Relatório de Decisões de Design: Batalha Naval

## Posicionamento dos Navios
Os navios nesse programa são posicionados de forma aleatória no tabuleiro oculto. Os tipos de navios e suas características (tamanho, símbolo, quantidade) são definidos em um dicionário chamado navios. Cada navio pode ter uma orientação horizontal ou vertical, decidida de forma aleatória.

## Controle das Jogadas
O controle das jogadas é gerido pela função "main()", que inicializa o jogo, gera os tabuleiros, e permite ao jogador escolher a dificuldade, o que determina o número de tentativas disponíveis.

A escolha da dificuldade é feita pelo usuário através de input, e o número de tentativas é ajustado de acordo com a escolha.

## Função Jogo
A função jogo é responsável pela lógica principal do jogo, controlando as tentativas do jogador, atualizando o tabuleiro e verificando acertos e destruições de navios.

Exibir o Tabuleiro: A cada tentativa, o tabuleiro é exibido.
<br>Selecionar Casa: O jogador escolhe uma casa do tabuleiro para atacar.
<br>Verificação de Acerto: Verifica-se se a casa selecionada contém parte de um navio. Caso positivo, o navio é atualizado e o jogador é informado.
<br>Atualizar Tentativas: O número de tentativas é decrementado.
<br>Verficação de Fim de Jogo: Se o jogador destruir todos os navios ou esgotar as tentativas, o jogo é encerrado e uma mensagem é exibida.

## Função Seleção de Casa
A função selecao_casa é responsável por receber e validar a entrada do jogador para selecionar uma casa no tabuleiro. Ela garante que a entrada seja válida e que a casa ainda não tenha sido escolhida.