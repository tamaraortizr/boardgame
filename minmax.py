infinito = 100000


class Minimax(object):

    def __init__(self, heuristic_eval):
        self.heuristic_eval = heuristic_eval

    def minimax(self, tablero, tableromaster, profundidad, jugador, oponente, alfa = -infinito, beta = infinito):
        bestoption = tablero
        if profundidad == 0:
            return self.heuristic_eval(tablero, tablero, profundidad, jugador, oponente), tablero
        for option in tablero.next_states(jugador):
            puntuacion, newoption = self.minimax(
                option, tablero, profundidad - 1, oponente, jugador, -beta, -alfa)
            puntuacion = -puntuacion
            if puntuacion > alfa:
                alfa = puntuacion
                bestoption = option
            if beta <= alfa:
                break
        return self.heuristic_eval(tablero, tablero, profundidad, jugador, oponente), bestoption
