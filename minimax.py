infinito = 100000


class Minimax(object):

    def __init__(self, heuristic_eval):
        self.heuristic_eval = heuristic_eval

    def minimax(self, tablero, tableromaster, profundidad, jugador, oponente, alfa = -infinito, beta = infinito):
        mejoropcion = tablero
        if profundidad == 0:
            return self.heuristic_eval(tableromaster, tablero, profundidad, jugador, oponente), tablero
        for opcion in tablero.siguientemov(jugador):
            puntuacion, nuevaopcion = self.minimax(opcion, tablero, profundidad - 1, oponente, jugador, -beta, -alfa)
            puntuacion = -puntuacion
            if puntuacion > alfa:
                alfa = puntuacion
                mejoropcion = opcion
            if beta <= alfa:
                break
        return self.heuristic_eval(tablero, tablero, profundidad, jugador, oponente), mejoropcion
