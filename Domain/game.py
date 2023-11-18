import tkinter as tk
from Domain.domino import *

class Juego:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        
        self.crear_fichas()
        self.dibujar()
    
    def crear_fichas(self):
        self.fichas = []
        for i in range(7):
            for j in range(i,7,1):
                print(f"ficha: {i}-{j}")
                self.fichas.append(Domino(j,i, i*90, j*90,40))

    def dibujar(self):
        for ficha in self.fichas:
            print(f"ficha: {ficha.number1}-{ficha.number2} loc: {ficha.x},{ficha.y}")
            ficha.paint(self.canvas)
        