from codecs import BufferedIncrementalEncoder
import pygame

from jogo.cores import CORES

class Paleta:
    def __init__(self, posicao, acao_subir, acao_descer):
        self.posicao = posicao
        self.subir = acao_subir
        self.descer = acao_descer

    def desenha(self, tela):
        pygame.draw.rect(
            tela,
            CORES.branco,
            self.posicao + [10, 150]
        )

    def movimenta(self, teclas):
        if teclas[self.subir] and self.posicao[1] != 0:
            self.posicao[1] -= 5

        if teclas[self.descer] and self.posicao[1] != 250:
            self.posicao[1] += 5
