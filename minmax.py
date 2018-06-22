infinito = 100000


class Minimax(objeto):


    def __init__(self, heuristic_eval):
        self.heuristic_eval = heuristic_eval


    def minimax(self, tablero, tableromaster, profundidad, jugador, oponente,
                alfa = -infinito, beta = infinito):
        bestChild = tablero
        if profundidad == 0:
            return (self.heuristic_eval(tablero, tablero, profundidad,
                                        jugador, oponente), tablero)
        for child in tablero.next_states(jugador):
            puntuacion, newChild = self.minimax(
                child, tablero, profundidad - 1, oponente, jugador, -beta, -alfa)
            puntuacion = -puntuacion
            if puntuacion > alfa:
                alfa = puntuacion
                bestChild = child
            if beta <= alfa:
                break
        return (self.heuristic_eval(tablero, tablero, profundidad, jugador,
                                    oponente), bestChild)
