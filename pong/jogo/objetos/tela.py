"""
"""
import pygame

from jogo.cores import CORES

class Tela:
    def __init__(self) -> None:
        self.tela = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Pong!")

    def renderiza(self, paletas, bola):
        self.tela.fill(CORES.preto)

        pygame.draw.line(
            self.tela,
            CORES.branco,
            [300, 40],
            [300, 360],
            3
        )

        bola.desenha(self.tela)

        for paleta in paletas:
            paleta.desenha(self.tela)

        pygame.display.update()