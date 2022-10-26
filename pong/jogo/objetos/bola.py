from codecs import BufferedIncrementalEncoder
import pygame

from jogo.cores import CORES

class Bola:
    def __init__(self):
        self.posicao = [300, 200]

    def desenha(self, tela):
        pygame.draw.circle(
            tela,
            CORES.vermelho,
            self.posicao,
            10
        )