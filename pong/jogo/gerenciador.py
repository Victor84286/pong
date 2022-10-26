"""
Realiza a orquestração do jogo e invoca os objetos
"""
import pygame

from .objetos.tela import Tela
from .objetos.paleta import Paleta
from .objetos.bola import Bola

class Gerenciador:
    def __init__    (self) -> None:
        self.inicia_partida()

    def inicia_partida(self):
        self.tela = Tela()
        self.paletas = [
            Paleta([20, 125], pygame.K_w, pygame.K_s),
            Paleta([570, 125], pygame.K_UP, pygame.K_DOWN)
            ]
        self.bola = Bola()

    def roda_jogo(self):
        while True:
            cliques = self.monitora_clicks()
            if pygame.QUIT in cliques:
                break

            self.trata_teclas_pressionadas()

            self.tela.renderiza(self.paletas, self.bola)

            pygame.time.Clock().tick(100)

    def trata_teclas_pressionadas(self):
        teclas = pygame.key.get_pressed()
        for paleta in self.paletas:
            paleta.movimenta(teclas)

    @staticmethod
    def monitora_clicks():
        cliques = []
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cliques.append(pygame.QUIT)

        return cliques