infinito = 100000

class Minmax(objeto):
    def inicio(self, heuristic_eval):
        self.heuristic_eval = heuristic_eval

    def minmax(self, board, masterboard, profundidad, jugador, oponente, a = -infinito, b = infinito ):
        bestChild = board
        if profundidad == 0:
            return (self.heuristic_eval(masterboard. board, profundidad, jugador, oponente), board)
        for n in board.next_states(jugador):
            puntaje, n = self.minmax()
        for child in board.next_states(player):
            score, newChild = self.minimax(
                child, board, depth - 1, opponent, player, -beta, -alfa)
            score = -score
            if score > alfa:
                alfa = score
                bestChild = child
            if beta <= alfa:
                break
        return (self.heuristic_eval(board, board, depth, player,
                                    opponent), bestChild)
