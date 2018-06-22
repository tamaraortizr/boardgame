import pygame
import sys
from pygame.locals import *
import time
from variables import azul, blanco, dificultad, humano, computadora
import os


class layout:
    def iniciar(self):
        self.tablero = tablero.Tablero()
        self.opciones()
