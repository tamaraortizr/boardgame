from variables import azul, blanco, vacio
from copy import deepcopy


class Tablero:

    def inicio(self):
        self.tablero = [[0, 0, 0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0, 0, 0,]]
        self.tablero[3][4] = azul
        self.tablero[4][3] = azul
        self.tablero[3][3] = blanco
        self.tablero[4][4] = blanco
        self.movvalido = []


    def objeto(self, f, c):
        return self.tablero[f][c]


    def posibles(self, fila, columna, color):
        if color == azul:
            otro = blanco
        else:
            otro = azul
        espacios = []
        if fila < 0 or fila > 7 or columna < 0 or columna > 7:
            return espacios
        f = fila - 1
        if f >= 0 and self.tablero[f][columna] == otro:
            f = f - 1
            while f >= 0 and self.tablero[f][columna] == otro:
                f = f - 1
            if f >= 0 and self.tablero[f][columna] == 0:
                espacios = espacios + [(f, columna)]
        f = fila - 1
        c = columna + 1
        if f >= 0 and c < 8 and self.tablero[f][c] == otro:
            f = f - 1
            c = c + 1
            while f >= 0 and c < 8 and self.tablero[f][c] == otro:
                f = f - 1
                c = c + 1
            if f >= 0 and c < 8 and self.tablero[f][c] == 0:
                espacios = espacios + [(f, c)]
        c = columna + 1
        if c < 8 and self.tablero[fila][c] == otro:
            c = c + 1
            while c < 8 and self.tablero[fila][c] == otro:
                c = c + 1
            if c < 8 and self.tablero[fila][c] == 0:
                espacios = espacios + [(fila, c)]
        f = fila + 1
        c = columna + 1
        if f < 8 and c < 8 and self.tablero[f][c] == otro:
            f = f + 1
            c = c + 1
            while f < 8 and c < 8 and self.tablero[f][c] == otro:
                f = f + 1
                c = c + 1
            if f < 8 and c < 8 and self.tablero[f][c] == 0:
                espacios = espacios + [(f, c)]
        f = fila + 1
        if f < 8 and self.tablero[f][columna] == otro:
            f = f + 1
            while f < 8 and self.tablero[f][columna] == otro:
                f = f + 1
            if f < 8 and self.tablero[f][columna] == 0:
                espacios = espacios + [(f, columna)]
        f = fila + 1
        c = columna - 1
        if f < 8 and c >= 0 and self.tablero[f][c] == otro:
            f = f + 1
            c = c - 1
            while f < 8 and c >= 0 and self.tablero[f][c] == otro:
                f = f + 1
                c = c - 1
            if f < 8 and c >= 0 and self.tablero[f][c] == 0:
                espacios = espacios + [(f, c)]
        c = columna - 1
        if c >= 0 and self.tablero[fila][c] == otro:
            c = c - 1
            while c >= 0 and self.tablero[fila][c] == otro:
                c = c - 1
            if c >= 0 and self.tablero[fila][c] == 0:
                espacios = espacios + [(fila, c)]
        f = f - 1
        c = columna - 1
        if f >= 0 and c >= 0 and self.tablero[f][c] == otro:
            f = f - 1
            c = c - 1
            while f >= 0 and c >= 0 and self.tablero[f][c] == otro:
                f = f - 1
                c = c - 1
            if f >= 0 and c >= 0 and self.tablero[f][c] == 0:
                espacios = espacios + [(f, c)]

        return espacios


    def movimientovalido(self, color):
        if color == azul:
            otro = blanco
        else:
            otro = azul
        espacios = []
        for f in range(8):
            for c in range(8):
                if self.tablero[f][c] == color:
                    espacios = espacios + self.posibles(f, c, color)
        espacios = list(set(espacios))
        self.movvalido = espacios
        return espacios


    def efectuarmovimiento(self, movimiento, color):
        if movimiento in self.movvalido:
            self.tablero[movimiento[0]][movimiento[1]] = color
            for n in range(1, 9):
                self.flip(n, movimiento, color)


    def cambiar(self, direccion, posicion, color):
        if direccion == 1:
            filainc = -1
            colinc = 0
        elif direccion == 2:
            filainc = -1
            colinc = 1
        elif direccion == 3:
            filainc = 0
            colinc = 1
        elif direccion == 4:
            filainc = 1
            colinc = 1
        elif direccion == 5:
            filainc = 1
            colinc = 0
        elif direccion == 6:
            filainc = 1
            colinc = -1
        elif direccion == 7:
            filainc = 0
            colinc = -1
        elif direccion == 8:
            filainc = -1
            colinc = -1
        espacios = []
        f = posicion[0] + filainc
        c = posicion[1] + colinc
        if color == blanco:
            otro = azul
        else:
            otro = blanco

        if f in range(8) and c in range(8) and self.tablero[f][c] == otro:
            espacios = espacios + [(f, c)]
            f = f + filainc
            c = c + colinc
            while f in range(8) and c in range(8) and self.tablero[f][c] == otro:
                espacios = espacios + [(f, c)]
                f = f + filainc
                c = c + colinc
            if f in range(8) and c in range(8) and self.tablero[f][c] == color:
                for pos in espacios:
                    self.tablero[pos[0]][pos[1]] = color

    def devolvercambios(self):
        blancos, azules, vacios = self.contarpiezas()
        return self.tablero, azules, blancos

    def juegotermino(self):
        blancos, azules, vacios = self.contarpiezas()
        if blancos == 0 or azules == 0 or vacios == 0:
            return True
        if self.movimientovalido(azul) == [] and self.movimientovalido(blanco) == []:
            return True
        return False

    def formartablero(self):
        for f in range(8):
            print(f, ' |', end=' ')
            for c in range(8):
                if self.tablero[f][c] == azul:
                    print('A', end=' ')
                elif self.tablero[f][c] == blanco:
                    print('B', end=' ')
                else:
                    print(' ', end=' ')
                print('|', end=' ')
            print()

    def contarpiezas(self):
        blancos = 0
        azules = 0
        vacios = 0
        for f in range(8):
            for c in range(8):
                if self.tablero[f][c] == blanco:
                    blancos += 1
                elif self.tablero[f][c] == azul:
                    azules += 1
                else:
                    vacios += 1
        return blancos, azules, vacios

    def comparar(self, otrotablero):
        tablerodif = Tablero()
        tablerodif.tablero[3][4] = 0
        tablerodif.tablero[3][3] = 0
        tablerodif.tablero[4][3] = 0
        tablerodif.tablero[4][4] = 0
        for f in range(8):
            for c in range(8):
                if otrotablero.tablero[f][c] != self.tablero[f][c]:
                    otrotablero.tablero[f][c] = otrotablero.tablero[f][c]
        return otrotablero

    def espaciosalcostado(self, color):
        ecostado = 0
        for x, y in [(a, b) for a in range(8) for b in range(8) if self.tablero[a][b] == color]:
            for f, c in [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1]]:
                if 0 <= x + f <= 7 and 0 <= y + c <= 7:
                    if self.tablero[x + f][y + c] == vacio:
                        ecostado += 1
        return ecostado

    def siguientemov(self, color):
        movvalido = self.movimientovalido(color)
        for movimiento in movvalido:
            nuevotablero = deepcopy(self)
            nuevotablero.efectuarmovimiento(movimiento, color)
            yield nuevotablero
