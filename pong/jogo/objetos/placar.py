import pygame

from jogo.cores import CORES

class Placar:
    def __init__(self) -> None:
        self.p1 = 0
        self.p2 = 0

    def atualiza(self, paletas, bola):
        """
        Atualiza o placar conforme a posição da bola e das paletas.
        Retorna True se o placar foi atualizado, e False se não foi.
        """
        if self.verifica_posicao(paletas[0], bola, 35):
            self.p2 += 1

            return True

        if self.verifica_posicao(paletas[1], bola, 565):
            self.p1 += 1

            return True

        return False

    def verifica_vencedor(self):
        if self.p1 + self.p2 == 5:
            if self.p1 > self.p2:
                return "Vitória do P1!"
            if self.p2 > self.p1:
                return "Vitória do P2!"

        return False

    def verifica_posicao(self, paleta, bola, limite):
        """
        Verifica se a bola está colidindo no limite e se está na paleta.
        Retorna False caso não esteja encontrando na paleta.
        """
        if bola.posicao[0] == limite:
            if paleta.posicao[1] <= bola.posicao[1] <= paleta.posicao[1] + paleta.tamanho_inicial[1]:
                return False

            return True

        return False

    def desenha(self, tela):
        fonte = pygame.font.SysFont(None, 30)

        p1_fonte = fonte.render(str(self.p1), True, CORES.vermelho)
        p2_fonte = fonte.render(str(self.p2), True, CORES.vermelho)

        tela.blit(p1_fonte, (5, 20))
        tela.blit(p2_fonte, (585, 20))

        # fonte texto vencedor
        fonte_vencedor = pygame.font.SysFont(None, 70)

        # tela final do jogo
        # com o vencedor e fundo preto
        if self.verifica_vencedor() != False:
            vencedor_fonte = fonte_vencedor.render(str(self.verifica_vencedor()), True, CORES.vermelho)
            tela.fill(CORES.preto)
            tela.blit(vencedor_fonte, (145, 170))