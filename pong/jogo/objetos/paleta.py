import pygame

from jogo.cores import CORES

class Paleta:
    def __init__(self, posicao, acao_subir, acao_descer, tamanho_inicial):
        self.posicao = posicao
        self.subir = acao_subir
        self.descer = acao_descer
        self.tamanho_inicial = tamanho_inicial

    def desenha(self, tela, tamanho):
        pygame.draw.rect(
            tela,
            CORES.branco,
            # [pos_x, pos_y, larg, alt]
            self.posicao + tamanho
        )

    def movimenta(self, teclas):
        if teclas[self.subir] and self.posicao[1] > 0:
            self.posicao[1] -= 5

        if teclas[self.descer] and self.posicao[1] < 400 - self.tamanho_inicial[1]:
            self.posicao[1] += 5
