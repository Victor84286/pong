"""Realiza a orquestração do jogo e invoca os objetos."""
import time

import pygame

from .objetos.bola import Bola
from .objetos.tela import Tela
from .objetos.placar import Placar
from .objetos.paleta import Paleta

class Gerenciador:
    def __init__(self) -> None:
        self.tela = Tela()
        self.placar = Placar()
        self.inicia_partida()

    def inicia_partida(self):
        self.paletas = [
            Paleta([20, 125], pygame.K_w, pygame.K_s, [10, 150]),
            Paleta([570, 125], pygame.K_UP, pygame.K_DOWN, [10, 150])
        ]
        self.bola = Bola()

    def roda_loop(self):
        while True:
            cliques = self.monitora_cliques()
            if pygame.QUIT in cliques:
                break

            self.trata_teclas_pressionadas()
            self.bola.movimenta()


            if self.placar.atualiza(self.paletas, self.bola):
                time.sleep(0.5)

                if self.placar.verifica_vencedor():    # verifica se houve vencedor
                    self.tela.renderiza(self.paletas, self.bola, self.placar)   # printa que houve vencedor
                    time.sleep(2.0)         # mantém a tela parada por 2 segundos
                    break           #finaliza o jogo

                self.inicia_partida()


            if self.bola.posicao[0] <= 35 or self.bola.posicao[0] >= 565:       # verifica batida nas paredes das barras
                self.bola.velocidade += 1                   # aumenta a velocidade da bola
                for paleta in self.paletas:                 # diminui o tamanho das barras
                    paleta.tamanho_inicial[1] -= 10

            self.tela.renderiza(self.paletas, self.bola, self.placar)

            pygame.time.Clock().tick(60)

    def trata_teclas_pressionadas(self):
        teclas = pygame.key.get_pressed()
        for paleta in self.paletas:
            paleta.movimenta(teclas)


    @staticmethod
    def monitora_cliques():
        cliques = []
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cliques.append(pygame.QUIT)

        return cliques

