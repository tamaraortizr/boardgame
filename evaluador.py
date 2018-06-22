from variables import blanco, azul, vacio

class Evaluador(object):
    perdertodo_puntuacion = 1000
    pieza_contador_peso = [0, 0, 0, 4, 1]
    posibles_peso = [5, 4, 3, 2, 0]
    movimientos_peso = [7, 6, 5, 4, 0]
    esquinas_peso = [35, 35, 35, 35, 0]
    lados_peso = [0, 3, 4, 5, 0]
    x_peso = [-8, -8, -8, -8, 0]

    def diferencial_piezas(self, dtablero, banda):
        if Evaluador.pieza_contador_peso[banda] != 0:
            whites, blacks, empty = dtablero.contarpiezas()
            if self.jugador == blanco:
                mipuntuacion = blancos
                tupuntuacion = azules
            else:
                mipuntuacion = azules
                tupuntuacion = blancos
            return Evaluador.pieza_contador_peso[banda] * (mipuntuacion - tupuntuacion)
        return 0

    def diferencial_esquinas(self, dcontar, dtablero, banda):
        if Evaluador.esquinas_peso[banda] != 0:
            mipuntuacion = 0
            tupuntuacion = 0
            for f in [0, 7]:
                for c in [0, 7]:
                    if dtablero.tablero[f][c] == self.jugador:
                        mipuntuacion += 1
                    elif dtablero.tablero[f][c] == self.oponente:
                        tupuntuacion += 1
                    if mipuntuacion + tupuntuacion >= dcontar:
                        break
                if mipuntuacion + tupuntuacion >= dcontar:
                    break
            return Evaluador.esquinas_peso[banda] * (mipuntuacion - tupuntuacion)
        return 0

    def diferencial_lados(self, dcontar, dtablero, banda):
        if Evaluador.lados_peso[banda] != 0:
            mipuntuacion = 0
            tupuntuacion = 0
            cuadrados = [(a, b) for a in [0, 7] for b in range(1, 7)] \
                + [(a, b) for a in range(1, 7) for b in [0, 7]]
            for x, y in cuadrados:
                if dtablero.tablero[x][y] == self.jugador:
                    mipuntuacion += 1
                elif dtablero.tablero[x][y] == self.oponente:
                    tupuntuacion += 1
                if mipuntuacion + tupuntuacion >= dcontar:
                    break
            return Evaluador.lados_peso[banda] * (mipuntuacion - tupuntuacion)
        return 0

    def diferencial_x(self, tableroinicio, tableroactual, dtablero, banda):
        if Evaluador.x_peso[banda] != 0:
            mipuntuacion = 0
            tupuntuacion = 0
            for x, y in [(a, b) for a in [1, 6] for b in [1, 6]]:
                if dtablero.tablero[x][y] != vacio and tableroinicio.tablero[x][y] == vacio:
                    esquinax = x
                    esquinay = y
                    if esquinax == 1:
                        esquinax = 0
                    elif esquinax == 6:
                        esquinax = 7
                    if esquinay == 1:
                        esquinay = 0
                    elif esquinay == 6:
                        esquinay = 7
                    if tableroactual.tablero[esquinax][esquinay] == vacio:
                        if tableroactual.tablero[x][y] == self.jugador:
                            mipuntuacion += 1
                        elif tableroactual.tablero[x][y] == self.oponente:
                            tupuntuacion += 1
            return Evaluador.x_peso[banda] * (mipuntuacion - tupuntuacion)
        return 0


    def diferencial_posibles(self, tableroinicio, tableroactual, banda):
        if Evaluador.posibles_peso[banda] != 0:
            mipuntuacion = tableroactual.espaciosalcostado(
                self.oponente) - tableroinicio.espaciosalcostado(self.oponente)
            tupuntuacion = tableroactual.espaciosalcostado(
                self.jugador) - tableroinicio.espaciosalcostado(self.jugador)
            return Evaluador.posibles_peso[banda] * (mipuntuacion - tupuntuacion)
        return 0


    def diferencial_movimientos(self, tableroinicio, tableroactual, banda):
        mipuntuacion = len(tableroactual.movimientovalido(self.jugador)) - \
            len(tableroinicio.movimientovalido(self.jugador))
        tupuntuacion = len(tableroactual.movimientovalido(
            self.oponente)) - len(tableroinicio.movimientovalido(self.oponente))
        return Evaluador.movimientos_peso[banda] * (mipuntuacion - tupuntuacion)

    def puntuacion(self, tableroinicio, tablero, profundidadactual, jugador, oponente):
        self.jugador = jugador
        self.oponente = oponente
        puntuacion = 0
        blancos, azules, vacio = tablero.contarpiezas()
        dtablero = tablero.comparar(tableroinicio)
        dcontar = sum(dtablero.contarpiezas())

        if (self.jugador == blancos and blancos == 0) or (self.jugador == azules and azules == 0):
            return -Evaluador.perdertodo_puntuacion
        if (self.oponente == blancos and blancos == 0) or (self.oponente == azules and azules == 0):
            return Evaluador.perdertodo_puntuacion

        npiezas = blancos + azules
        banda = 0
        if npiezas <= 16:
            banda = 0
        elif npiezas <= 32:
            banda = 1
        elif npiezas <= 48:
            banda = 2
        elif npiezas <= 64 - profundidadactual:
            banda = 3
        else:
            banda = 4

        puntuacion += self.diferencial_piezas(dtablero, banda)
        puntuacion += self.diferencial_esquinas(dcontar, dtablero, banda)
        puntuacion += self.diferencial_lados(dcontar, dtablero, banda)
        puntuacion += self.diferencial_x(tableroinicio,tablero, dtablero, banda)
        puntuacion += self.diferencial_posibles(tableroinicio, tablero, banda)
        puntuacion += self.diferencial_movimientos(tableroinicio, tablero, banda)
        return puntuacion
