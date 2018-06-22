import pygame
import graphics
import jugador
import tablero
from variables import azul, blanco


class Juego:

    def __init__(self):
        self.graphics = graphics.Graphics()
        self.tablero = tablero.Tablero()
        self.obteneropciones()

    def obteneropciones(self):
        jugador1, jugador2, nivel = self.graphics.mostraropciones()
        if jugador1 == "humano":
            self.jugadoractual = jugador.Humano(self.graphics, azul)
        else:
            self.jugadoractual = jugador.Computadora(azul, nivel + 3)
        if jugador2 == "humano":
            self.otrojugador = jugador.Humano(self.graphics, blanco)
        else:
            self.otrojugador = jugador.Computadora(blanco, nivel + 3)

        self.graphics.mostrarjuego()
        self.graphics.update(self.tablero.tablero, 2, 2)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            if self.tablero.juegotermino():
                blancos, azules, vacios = self.tablero.contarpiezas()
                if blancos > azules:
                    ganador = blanco
                elif azules > blancos:
                    ganador = azul
                else:
                    ganador = None
                break
            self.jugadoractual.obtenertableroactual(self.tablero)
            if self.tablero.movimientovalido(self.jugadoractual.color) != []:
                puntuacion, self.tablero = self.jugadoractual.obtenermovida()
                blancos, azules, vacios = self.tablero.contarpiezas()
                self.graphics.update(self.tablero.tablero, azules, blancos)
            self.jugadoractual, self.otrojugador = self.otrojugador, self.jugadoractual
        self.graphics.mostrarganador(ganador)
        pygame.time.wait(1000)
        self.restart()

    def restart(self):
        self.tablero = tablero.Tablero()
        self.obteneropciones()
        self.run()


def main():
    game = Juego()
    game.run()

if __name__ == '__main__':
    main()

