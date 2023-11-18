import tkinter as tk
from PIL import Image
from Domain.dots import Dots

VERTICAL_N1_N2 = 0
VERTICAL_N2_N1 = 1
HORIZONTAL_N1_N2 = 2

class Domino:
    def __init__(self, number1, number2, x, y, proportion) -> None:
        self.number1 = number1
        self.number2 = number2
        self.number1_active = False
        self.number2_active = False
        self.x = x
        self.y = y 
        self.proportion = proportion #value asigned to width and height
        self.orientation = HORIZONTAL_N1_N2

    def setGraphics(self, x, y, proportion):
        self.x = x
        self.y = y 
        self.proportion = proportion


    def vertical_n1_n2(self, canvas):
        Dots(self.x, self.y, self.proportion, self.number1, canvas, False)
        Dots(self.x, self.y+self.proportion, self.proportion, self.number2, canvas, False)
    
    def vertical_n2_n1(self, canvas):
        Dots(self.x, self.y, self.proportion, self.number2, canvas, False)
        Dots(self.x, self.y+self.proportion, self.proportion, self.number1, canvas, False)

    def horizontal_n1_n2(self, canvas):
        Dots(self.x, self.y, self.proportion, self.number1, canvas, True)
        Dots(self.x+self.proportion, self.y, self.proportion, self.number2, canvas, True)

    def paint(self, canvas):
        #self.vertical_n2_n1(canvas=canvas)

        # Calculate the total width and height for the new image
        width = self.proportion
        height = self.proportion

        if self.orientation == VERTICAL_N1_N2 or self.orientation == VERTICAL_N2_N1:
            height = height*2
        else:
            width = width*2
        
        # Create a new image with the calculated size
        new_image = tk.Canvas(canvas, width=width, height=height)

        switch = {
            VERTICAL_N1_N2: self.vertical_n1_n2,
            VERTICAL_N2_N1: self.vertical_n2_n1,
            HORIZONTAL_N1_N2: self.horizontal_n1_n2
        }

        draw = switch.get(self.orientation, self.horizontal_n1_n2)

        draw(canvas)
        
        return new_image