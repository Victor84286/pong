import pygame

from jogo.gerenciador import Gerenciador


def inicia_jogo():

    pygame.init()
    return Gerenciador()

def encerra_jogo():
    print("Encerrando o jogo!")
    pygame.quit()

def jogo():
    gerenciador = inicia_jogo()
    gerenciador.roda_jogo()
    encerra_jogo()

if __name__ == "__main__":
    jogo()