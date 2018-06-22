from evaluador import Evaluador
from variables import blanco, azul
from minimax import Minimax
import random


def cambiarcolor(color):
    if color == azul:
        return blanco
    else:
        return azul


class Humano:
    def __init__(self, graphics, color="azul"):
        self.color = color
        self.graphics = graphics

    def obtenermovida(self):
        movvalido = self.tablero_actual.movimientovalido(self.color)
        while True:
            movimiento = self.graphics.movimientomouse()
            if movimiento in movvalido:
                break
        self.tablero_actual.efectuarmovimiento(movimiento, self.color)
        return 0, self.tablero_actual

    def obtenertableroactual(self, tablero):
        self.tablero_actual = tablero


class Computadora(object):

    def __init__(self, color, prune=3):
        self.limiteprofundidad = prune
        evaluador = Evaluador()
        self.minimaxObj = Minimax(evaluador.puntuacion)
        self.color = color

    def obtenertableroactual(self, tablero):
        self.tablero_actual = tablero

    def obtenermovida(self):
        return self.minimaxObj.minimax(self.tablero_actual, None, self.limiteprofundidad, self.color, cambiarcolor(self.color))


class JugadorRandom (Computadora):

    def obtenermovida(self):
        x = random.sample(self.tablero_actual.movimientovalido(self.color), 1)
        return x[0]
